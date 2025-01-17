from flask import Flask, render_template, request, jsonify
from data import exam_details
from flask_cors import CORS
import json
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Load and initiate the general model
model = None
corpus_embeddings = None
urls = []

def initiate_general_model():
    global urls
    global model
    global corpus_embeddings
 
    with open('General_Dataset.json', 'r', encoding='utf-8', errors='ignore') as file:
        data = json.load(file)
 
    corpus = [entry['input'] for entry in data]
    urls = [entry['response'] for entry in data]
 
    # Dynamically download the model
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
 
    corpus_embeddings = model.encode(corpus, convert_to_tensor=True)
    print("General model initialized.")

def search_general(query):
    query_embedding = model.encode(query, convert_to_tensor=True)
    cosine_scores = cos_sim(query_embedding, corpus_embeddings)
    max_score = cosine_scores.max().item()  # Convert tensor value to float
    best_match_idx = cosine_scores.argmax().item()  # Convert tensor index to int

    if max_score < 0.35:
        return "Exam not found", max_score
    return urls[best_match_idx], max_score

# Routes
@app.route("/")
def index():
    return "Server running"

@app.route("/api/chatbot1", methods=["POST"])
def chat():
    if request.method == "POST":
        data = request.get_json()  # Get JSON data
        msg = data.get("msg")  # Retrieve the message from JSON
        if msg:
            response = get_exam_details(msg)
            if response == "Exam not found. Please check the name and try again.":
                # If exam is not found, calculate cosine similarity score
                best_match_url, max_score = search_general(msg)
                if best_match_url == "Exam not found" and max_score < 0.35:
                    return jsonify({"response": "Exam not found."})
                else:
                    return jsonify({"response": f"{best_match_url}"})
            return response
        return jsonify({"response": "Message not provided."}), 400
    return jsonify({"response": "Invalid request."}), 400

def get_exam_details(exam_name):
    exam_name = exam_name.strip().lower()  # Trim spaces and make lowercase

    for exam, details in exam_details.items():
        # Check if the exam keyword is present in the input message
        if exam.lower() in exam_name:
            response = {}
            if "start date" in exam_name or "starting date" in exam_name:
                response["start_date"] = details["start_date"]
            elif "end date" in exam_name or "ending date" in exam_name:
                response["end_date"] = details["end_date"]
            elif "link" in exam_name:
                response["link_details"] = {
                    "url": details["url"],
                    "apply_link": details["apply"]
                }
            elif "date" in exam_name:
                response["start_date"] = details["start_date"]
                response["end_date"] = details["end_date"]
            else:
                response["exam_details"] = {
                    "url": details["url"],
                    "start_date": details["start_date"],
                    "end_date": details["end_date"],
                    "apply_link": details["apply"]
                }

            # Return the response in JSON format using jsonify
            return jsonify(response)

    return "Exam not found. Please check the name and try again."

# Initialize the general model
initiate_general_model()

if __name__ == '__main__':
    app.run(debug=True)

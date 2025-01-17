from flask import Flask, render_template, request, jsonify
from data import exam_details
import time
from flask_cors import CORS


app = Flask(__name__)
# Enable CORS for all routes or specific origins
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def index():
    return "Server running"

@app.route("/api/chatbot", methods=["POST"])
def chat():
    if request.method == "POST":
        data = request.get_json()  # Get JSON data
        msg = data.get("msg")  # Retrieve the message from JSON
        if msg:
            response = get_exam_details(msg) 
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
                response["start_date"] = {
                    "name":exam_name,
                    "start_date": details["start_end"],
                }
            elif "end date" in exam_name or "ending date" in exam_name:
                response["end_date"] = {
                    "name":exam_name,
                    "end_date": details["end_date"],
                }
            elif "link" in exam_name:
                response["link_details"] = {
                    "name":exam_name,
                    "url": details["url"],
                    "apply_link": details["apply"]
                }

            elif "date" in exam_name:
                response["date"] = {
                    "name":exam_name,
                    "start_date": details["start_date"],
                    "end_date": details["end_date"],
                }
            else:
                response["exam_details"] = {
                    "name":details["name"],
                    "url": details["url"],
                    "start_date": details["start_date"],
                    "end_date": details["end_date"],
                    "apply_link": details["apply"]
                }

            # Return the response in JSON format using jsonify
            return jsonify(response)

    return jsonify({"response": "Exam not found. Please check the name and try again."})

if __name__ == '__main__':
    app.run(debug=True)
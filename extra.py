import json
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
from data import exam_details  # Import exam_details from data.py


# Initialize the model and global variables
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

    model = SentenceTransformer('all-MiniLM-L6-v2')
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

def get_exam_details(exam_name, exam_details):
    exam_name = exam_name.strip().lower()  # Trim spaces and make lowercase

    for exam, details in exam_details.items():
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
            return response
    return "Exam not found. Please check the name and try again."

if __name__ == "__main__":
    # Initialize the general model
    initiate_general_model()

    # Start while loop for continuous user interaction
    while True:
        query = input("\nEnter your query (type 'exit' to end): ")
        if query.strip().lower() == "exit":
            print("Exiting the program. Goodbye!")
            break

        # Check for exam details
        details = get_exam_details(query, exam_details)
        if details == "Exam not found. Please check the name and try again.":
            # If not found in exam_details, search the general dataset
            best_match_url, max_score = search_general(query)
            if best_match_url == "Exam not found" and max_score < 0.35:
                print("Response: Exam not found.")
            else:
                print(f"Response: {best_match_url}\nCosine Similarity Score: {max_score}")
        else:
            print(f"Exam Details:\n{json.dumps(details, indent=2)}")

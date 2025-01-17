import json
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

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

    print("General model running")

def search_general(query):
    query_embedding = model.encode(query, convert_to_tensor=True)

    cosine_scores = cos_sim(query_embedding, corpus_embeddings)

    max_score = cosine_scores.max().item()  # Get the maximum score as a Python float
    print(f"Max cosine similarity score: {max_score}")

    # Check the threshold
    if max_score < 0.35:
        return "Exam not found"

    best_match_idx = cosine_scores.argmax().item()  # Get the index of the best match
    return urls[best_match_idx]

if __name__ == '__main__':
    initiate_general_model()
    while True:
        query = input("Enter your query: ")
        best_match_url = search_general(query)
        print(f"Best match URL: {best_match_url}")

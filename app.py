import pymongo
import json
import re
from bson.objectid import ObjectId
from flask import Flask, request, jsonify
from flask_cors import CORS
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
from abbreviation_mapper import create_abbreviation_mapping, find_organization_by_input

class ExamLookupService:
    def __init__(self):
        # Initialize MongoDB connection
        self.client = pymongo.MongoClient("mongodb+srv://insansabddp:3SqXcP41pHBjR0nH@cluster0.zz4x9.mongodb.net/GovernmentProject?retryWrites=true&w=majority&appName=Cluster0")
        self.db = self.client['GovernmentProject']
        self.organizations_collection = self.db['organizations']
        self.events_collection = self.db['events']
        
        # Initialize semantic search components
        self.model = None
        self.corpus_embeddings = None
        self.urls = []
        
        # Create abbreviation mapping
        self.abbreviation_map = create_abbreviation_mapping(self.organizations_collection)
        
        # Initialize the semantic search model
        self._initialize_semantic_model()
    
    def _initialize_semantic_model(self):
        """Initialize the semantic search model with dataset."""
        try:
            with open('General_Dataset.json', 'r', encoding='utf-8', errors='ignore') as file:
                data = json.load(file)
            
            corpus = [entry['input'] for entry in data]
            self.urls = [entry['response'] for entry in data]
            
            # Load the model
            self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
            self.corpus_embeddings = self.model.encode(corpus, convert_to_tensor=True)
            return True
        except Exception as e:
            print(f"Error initializing semantic model: {e}")
            return False
    
    def _search_general(self, query):
        """Perform semantic search on the general dataset."""
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        cosine_scores = cos_sim(query_embedding, self.corpus_embeddings)
        max_score = cosine_scores.max().item()
        best_match_idx = cosine_scores.argmax().item()

        if max_score < 0.35:
            return "Exam not found", max_score
        return self.urls[best_match_idx], max_score
    
    def _is_math_question(self, msg):
        """Check if the input is a mathematical question."""
        return bool(re.search(r'[\d\+\-\*/\s]+$', msg))
    
    def _extract_math_expression(self, msg):
        """Extract mathematical expression from input."""
        match = re.findall(r'[\d\+\-\*/]+', msg.replace(" ", ""))
        return "".join(match) if match else None
    
    def _solve_math_problem(self, msg):
        """Solve a mathematical problem."""
        try:
            math_expression = self._extract_math_expression(msg)
            if math_expression:
                return eval(math_expression)
            return "Invalid math problem."
        except Exception:
            return "Invalid math problem."
    
    def process_user_input(self, user_input):
        """Process user input and return appropriate response."""
        # Check if it's a math question
        if self._is_math_question(user_input):
            answer = self._solve_math_problem(user_input)
            return {"response": f"The answer is: {answer}"}, None, None
        
        # Try to find organization using mapping
        organization = find_organization_by_input(
            self.organizations_collection, 
            user_input, 
            self.abbreviation_map
        )
        
        if organization:
            if 'events' in organization and organization['events']:
                event_ids = organization['events']
                
                # Format response for API
                events = []
                for i, event_id in enumerate(event_ids):
                    event = self.events_collection.find_one({'_id': event_id})
                    if event and 'name' in event:
                        events.append({
                            "name": event['name'], 
                            "id": str(event_id)
                        })
                
                return {
                    "organization": {
                        "name": organization['name'],
                        "abbreviation": organization['abbreviation']
                    },
                    "events": events
                }, organization, event_ids
            else:
                return {"message": f"No present events for {organization['name']} ({organization['abbreviation']})"}, None, None
        else:
            # If not found using abbreviation mapping, try semantic search
            result, confidence = self._search_general(user_input)
            
            if result != "Exam not found":
                return {"message": result}, None, None
            else:
                return {"message": "No matching exam found. Please try a different search term."}, None, None
    
    def get_event_details(self, event_id):
        """Get formatted details for a specific event."""
        try:
            # Convert string ID to ObjectId if necessary
            if isinstance(event_id, str):
                event_id = ObjectId(event_id)
                
            event = self.events_collection.find_one({'_id': event_id})
            if not event:
                return {"error": "Event not found."}
                
            # Convert ObjectId to string for JSON serialization
            event_details = {key: str(value) if isinstance(value, ObjectId) else value 
                            for key, value in event.items() 
                            if key not in ['document_links', 'details']}
            
            return event_details
        except Exception as e:
            return {"error": f"Error retrieving event details: {str(e)}"}
    
    def get_event_by_name_and_index(self, exam_name, event_index):
        """Get event by event name and index."""
        try:
            # First check if the exam_name is actually an event name
            event_index = int(event_index)
            
            # Try to find an exact match for the event name
            event = self.events_collection.find_one({"name": exam_name})
            if event:       
                return self.get_event_details(event['_id'])
            
            # If not found directly, try to find organization by name or abbreviation
            organization = self.organizations_collection.find_one({"name": exam_name}) or \
                          self.organizations_collection.find_one({"abbreviation": exam_name})
            
            if organization and 'events' in organization and organization['events']:
                event_ids = organization['events']
                
                if 0 <= event_index < len(event_ids):
                    selected_event_id = event_ids[event_index]
                    return self.get_event_details(selected_event_id)
                else:
                    return {"error": f"Please enter a number between 0 and {len(event_ids)-1}."}
            
            # If still not found, try to find events with similar names
            events_cursor = self.events_collection.find({"name": {"$regex": exam_name, "$options": "i"}})
            events_list = list(events_cursor)
            
            if events_list:
                # If we found events with similar names, return the one at the specified index
                if 0 <= event_index < len(events_list):
                    return self.get_event_details(events_list[event_index]['_id'])
                else:
                    return {"error": f"Please enter a number between 0 and {len(events_list)-1}."}
            
            # If all else fails, return error
            return {"error": "Organization or event not found"}
        except ValueError:
            # If not a valid index, return error
            return {"error": "Invalid event index"}
        except Exception as e:
            return {"error": f"Error processing request: {str(e)}"}


# Initialize the Flask application
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Create exam lookup service
exam_service = ExamLookupService()

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "Server is running"})

# @app.route('/api/chatbot', methods=['POST'])
# def chatbot():
#     data = request.get_json()
#     user_input = data.get('query', '')
#     response, organization, event_ids = exam_service.process_user_input(user_input)
    
#     # Create an array of names to return
#     names = []
    
#     # Check if response contains events
#     if "events" in response:
#         # Extract event names from the events list
#         names = [event["name"] for event in response["events"]]
#     # If it's a message response, add the message to names array
#     elif "message" in response:
#         names.append(response["message"])
#     # If it's a math problem response, add the answer
#     elif "response" in response:
#         names.append(response["response"])
    
#     return jsonify(names)

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_input = data.get('query', '')
    response, organization, event_ids = exam_service.process_user_input(user_input)
    
    # Return the original response object directly
    return jsonify(response)

@app.route('/api/chatbot/event', methods=['POST'])
def event_details():
    data = request.get_json()
    
    # The request can contain either event_id OR (examname + index)
    event_id = data.get('event_id')
    
    if event_id:
        # Direct event ID lookup
        response = exam_service.get_event_details(event_id)
    else:
        # Lookup by examname and index
        exam_name = data.get('examname', '')
        event_index = data.get('index',0)
        response = exam_service.get_event_by_name_and_index(exam_name, event_index)
    
    return jsonify(response)

# # Add a new endpoint that works directly with event IDs
# @app.route('/api/chatbot/event/<event_id>', methods=['GET'])
# def event_details_by_id(event_id):
#     response = exam_service.get_event_details(event_id)
#     return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
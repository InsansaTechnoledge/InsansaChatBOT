from flask import Flask, request, jsonify
from data import exam_details
import time
from flask_cors import CORS
from datetime import datetime
import numpy as np
from functools import lru_cache
from concurrent.futures import ThreadPoolExecutor
import os
import sys
import traceback
import json
from pathlib import Path

# Create Flask app
app = Flask(__name__)

# Initialize CORS
CORS(app, resources={r"/*": {"origins": "*"}})

from synonym_handler import SynonymHandler

# Initialize components with error handling
try:
    synonym_handler = SynonymHandler()
    thread_pool = ThreadPoolExecutor(max_workers=4)
    response_cache = {}
    print("Components initialized successfully")
except Exception as e:
    print(f"Component initialization failed: {str(e)}")
    sys.exit(1)

# Global cache for variation embeddings
variation_embeddings = {}
exam_variations_map = {}

@lru_cache(maxsize=1000)
def get_cached_embedding(text):
    """Cache embeddings using LRU cache"""
    try:
        return synonym_handler.get_embedding(text)
    except Exception as e:
        print(f"Error getting embedding for text: {str(e)}")
        return None

def initialize_embeddings():
    """Precompute embeddings for all exam variations"""
    global variation_embeddings, exam_variations_map
    all_variations = []
    
    try:
        def process_exam(exam_key):
            variations = synonym_handler.generate_variations(exam_key)
            return exam_key, variations

        with ThreadPoolExecutor(max_workers=4) as executor:
            results = list(executor.map(process_exam, exam_details.keys()))

        for exam_key, variations in results:
            all_variations.extend(variations)
            for variation in variations:
                exam_variations_map[variation] = exam_key

        variation_embeddings = {
            variation: get_cached_embedding(variation)
            for variation in all_variations
        }

        print(f"Successfully initialized {len(all_variations)} variations")
        return exam_variations_map

    except Exception as e:
        print(f"Error during embedding initialization: {str(e)}")
        return {}

def extract_intent(query: str) -> str:
    """Extract intent using optimized keyword matching"""
    query_lower = query.lower()
    intent_keywords = {
        'start_date': {'start', 'begin', 'when', 'commence', 'conducted', 'dates'},
        'end_date': {'end', 'finish', 'close', 'last', 'till', 'until', 'deadline', 'ends'},
        'link': {'link', 'website', 'apply', 'register', 'portal', 'application', 'process'}
    }
    
    for intent, keywords in intent_keywords.items():
        if any(keyword in query_lower for keyword in keywords):
            return intent
    return 'general'

def find_best_match(query_embedding, threshold=0.6):
    """Find best matching exam using vectorized operations"""
    try:
        similarities = {
            exam_key: np.max([
                np.dot(query_embedding, variation_embeddings[variation])
                for variation in synonym_handler.generate_variations(exam_key)
            ])
            for exam_key in exam_details.keys()
        }
        
        best_match = max(similarities.items(), key=lambda x: x[1])
        return best_match if best_match[1] > threshold else (None, 0)
    except Exception as e:
        print(f"Error finding best match: {str(e)}")
        return (None, 0)

def get_exam_type(exam_name):
    """Get exam type based on exam details and synonyms"""
    exam_info = exam_details.get(exam_name, {})
    url = exam_info.get('url', '').lower()
    
    if any(keyword in url for keyword in ['entrance', 'admission', 'education', 'neet', 'jee']):
        return 'entrance'
    elif any(keyword in url for keyword in ['recruitment', 'careers', 'jobs', 'vacancy']):
        return 'job'
    return 'general'

def get_context_words(exam_type):
    """Get context words based on exam type"""
    common_words = ['it', 'this', 'the']
    
    if exam_type == "entrance":
        base_words = ['application', 'admission', 'registration', 'form', 'process', 'fee', 'dates', 'schedule']
        variations = []
        for word in base_words:
            variations.extend(synonym_handler.generate_variations(word))
        return common_words + list(set(variations))
    
    elif exam_type == "job":
        base_words = ['position', 'vacancy', 'post', 'recruitment', 'application', 'deadline']
        variations = []
        for word in base_words:
            variations.extend(synonym_handler.generate_variations(word))
        return common_words + list(set(variations))
    
    else:
        base_words = ['exam', 'test', 'application']
        variations = []
        for word in base_words:
            variations.extend(synonym_handler.generate_variations(word))
        return common_words + list(set(variations))

def is_context_dependent(msg, exam_type):
    """Check if message is context dependent based on exam type using embeddings"""
    context_words = get_context_words(exam_type)
    msg_embedding = synonym_handler.get_embedding(msg)
    
    for word in context_words:
        word_embedding = synonym_handler.get_embedding(word)
        similarity = np.dot(msg_embedding, word_embedding)
        if similarity > 0.6:
            return True
    
    return False

def get_last_exam_context(recent_chats):
    """Get the most recently discussed exam from chat history"""
    if not recent_chats:
        return None
        
    for chat in reversed(recent_chats):
        message = chat['message'].lower()
        response = chat['response'].lower()
        
        for exam_key in exam_details.keys():
            if exam_key.lower() in message:
                return exam_key
                
        for exam_key in exam_details.keys():
            if exam_key.lower() in response.split()[0:3]:
                return exam_key
                
    return None

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "online",
        "message": "Chatbot API is running. Use /api/chatbot1 endpoint for queries.",
        "endpoints": {
            "/api/chatbot1": "POST - Send chat queries",
            "/": "GET - Service status"
        }
    })

# Create a sessions directory if it doesn't exist
SESSIONS_DIR = Path("chat_sessions")
SESSIONS_DIR.mkdir(exist_ok=True)

def get_session_file(user_id, session_id):
    """Get the path for a session's JSON file"""
    return SESSIONS_DIR / f"{user_id}_{session_id}.json"

def save_chat_to_session(user_id, message, response):
    """Save chat message and response to session file"""
    try:
        session_id = datetime.now().strftime('%Y%m%d')
        session_file = get_session_file(user_id, session_id)
        
        if session_file.exists():
            with open(session_file, 'r') as f:
                session_data = json.load(f)
        else:
            session_data = {
                "user_id": user_id,
                "session_id": session_id,
                "chat_history": []
            }
        
        chat_entry = {
            "message": message,
            "response": response,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        session_data["chat_history"].append(chat_entry)
        
        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2)
            
    except Exception as e:
        print(f"Error saving chat to session: {str(e)}")

def get_recent_chats(user_id, limit=3):
    """Get recent chats from current session file"""
    try:
        session_id = datetime.now().strftime('%Y%m%d')
        session_file = get_session_file(user_id, session_id)
        
        if session_file.exists():
            with open(session_file, 'r') as f:
                session_data = json.load(f)
                # Return last 'limit' chats
                chats = session_data["chat_history"][-limit:]
                return [{
                    "message": chat["message"],
                    "response": chat["response"],
                    "timestamp": chat["timestamp"]
                } for chat in chats]
        return []
        
    except Exception as e:
        print(f"Error getting recent chats: {str(e)}")
        return []

@app.route("/api/chatbot1", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_id = data.get("user_id", "default_user")
        msg = data.get("msg")
        
        if not msg:
            return jsonify({"response": "Message not provided."}), 400

        # Get recent chats from session file
        recent_chats = get_recent_chats(user_id, limit=3)

        # Process message with context
        processed_msg = msg.lower()

        # Check if current message directly mentions an exam or its variations
        direct_exam_mention = None
        for exam_key in exam_details.keys():
            if any(variation.lower() in processed_msg 
                  for variation in synonym_handler.generate_variations(exam_key)):
                direct_exam_mention = exam_key
                break

        if direct_exam_mention:
            current_context = direct_exam_mention
        else:
            current_context = get_last_exam_context(recent_chats)
            if current_context:
                exam_type = get_exam_type(current_context)
                if is_context_dependent(msg, exam_type):
                    processed_msg = f"{current_context} {processed_msg}"

        query_embedding = get_cached_embedding(processed_msg)
        if query_embedding is None:
            return jsonify({"response": "Error processing query. Please try again."})

        best_match, score = find_best_match(query_embedding)

        if not best_match and current_context:
            best_match = current_context
        elif not best_match:
            # Try checking synonyms variations one more time
            for exam_key, exam_info in exam_details.items():
                variations = synonym_handler.exam_fullforms.get(exam_key, [])
                variations.extend(synonym_handler.generate_variations(exam_key))
                msg_terms = processed_msg.lower().split()
                if any(any(term in variation.lower() for term in msg_terms) 
                      for variation in variations):
                    best_match = exam_key
                    break
            if not best_match:
                return jsonify({"response": "Exam not found. Please check the name and try again."})

        # Get exam details and prepare response
        exam = exam_details[best_match]
        intent = extract_intent(msg)

        # Prepare response based on intent
        if intent == 'start_date' and 'start_date' in exam:
            response = f"The {best_match} starts from {exam['start_date']}"
        elif intent == 'end_date' and 'end_date' in exam:
            response = f"The {best_match} ends on {exam['end_date']}"
        elif intent == 'link':
            response = f"You can find details about {best_match} at: {exam['url']}\nApplication link: {exam['apply']}"
        else:
            response = f"Details for {best_match}:"
            if 'start_date' in exam:
                response += f"\nStart Date: {exam['start_date']}"
            if 'end_date' in exam:
                response += f"\nEnd Date: {exam['end_date']}"
            response += f"\nMore Info: {exam['url']}\nApply here: {exam['apply']}"

        # Save chat and return response
        try:
            save_chat_to_session(user_id, msg, response)
            recent_chats = get_recent_chats(user_id, limit=3)
            
            response_data = {
                "response": response,
                "chat_history": list(reversed(recent_chats))
            }
            return jsonify(response_data)
        except Exception as e:
            print(f"Error preparing response: {str(e)}")
            return jsonify({"response": response})

    except Exception as e:
        print(f"Error processing request: {str(e)}")
        traceback.print_exc()
        return jsonify({"response": "An error occurred. Please try again."}), 500

if __name__ == '__main__':
    print("Starting Flask application...")
    try:
        print("Initializing embeddings...")
        exam_variations_map = initialize_embeddings()
        print("Initialization complete!")
        
        port = int(os.environ.get('PORT', 8000))
        print(f"Starting server on port {port}...")
        app.run(debug=True, host='0.0.0.0', port=port, use_reloader=False)
    except Exception as e:
        print(f"Error during startup: {str(e)}")
        sys.exit(1)
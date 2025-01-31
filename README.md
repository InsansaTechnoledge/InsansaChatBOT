# Educational and Job Exam Chatbot

A Flask-based chatbot API that provides information about various educational and job-related exams in India.

## Features

- Provides exam details, dates, and application links
- Handles context-aware queries
- Supports multiple exam variations and synonyms
- Session-based chat history
- Semantic similarity for query matching

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd exam-chatbot
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Start the server:
```bash
python app.py
```

## API Usage

Send POST requests to `/api/chatbot1` with JSON body:
```json
{
    "user_id": "test_user",
    "msg": "When is NEET conducted?"
}
```

Example response:
```json
{
    "response": "The NEET starts from Mid-February 2025",
    "chat_history": [
        {
            "message": "When is NEET conducted?",
            "response": "The NEET starts from Mid-February 2025",
            "timestamp": "2025-01-31 12:44:09"
        }
    ]
}
```

## Usage Examples

### Research Organizations (BARC)
```bash
# Initial query
curl -X POST -H "Content-Type: application/json" -d "{\"user_id\": \"test_user\", \"msg\": \"BARC recruitment details\"}" http://localhost:8000/api/chatbot1

# Follow-up about application
curl -X POST -H "Content-Type: application/json" -d "{\"user_id\": \"test_user\", \"msg\": \"How to apply for it?\"}" http://localhost:8000/api/chatbot1
```

### Defense Exams (CDS)
```bash
# Ask about exam dates
curl -X POST -H "Content-Type: application/json" -d "{\"user_id\": \"test_user\", \"msg\": \"When is CDS exam?\"}" http://localhost:8000/api/chatbot1

# Ask about end date
curl -X POST -H "Content-Type: application/json" -d "{\"user_id\": \"test_user\", \"msg\": \"When does it end?\"}" http://localhost:8000/api/chatbot1
```

### Research Fellowship (KVPY)
```bash
# Initial query
curl -X POST -H "Content-Type: application/json" -d "{\"user_id\": \"test_user\", \"msg\": \"When is KVPY conducted?\"}" http://localhost:8000/api/chatbot1

# Ask about important dates
curl -X POST -H "Content-Type: application/json" -d "{\"user_id\": \"test_user\", \"msg\": \"What are the important dates?\"}" http://localhost:8000/api/chatbot1
```

### Banking Sector (SBI)
```bash
# Get exam information
curl -X POST -H "Content-Type: application/json" -d "{\"user_id\": \"test_user\", \"msg\": \"Tell me about SBI exam\"}" http://localhost:8000/api/chatbot1

# Ask about registration
curl -X POST -H "Content-Type: application/json" -d "{\"user_id\": \"test_user\", \"msg\": \"What's the registration process?\"}" http://localhost:8000/api/chatbot1
```

The chatbot maintains context between messages, so you can ask follow-up questions without repeating the exam name. It supports various types of queries:
- Exam dates and schedules
- Application process
- Registration links
- General exam information
```

## Project Structure

- `app.py`: Main Flask application
- `data.py`: Exam details and variations
- `synonym_handler.py`: Handles exam name variations and semantic matching
- `chat_sessions/`: Directory for storing chat session files
- `requirements.txt`: Project dependencies

## Technologies Used

- Flask
- SQLAlchemy
- Sentence Transformers
- NLTK
- NumPy

## Environment Variables

- `PORT`: Server port (default: 8000)

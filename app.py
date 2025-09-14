from flask import Flask, jsonify
import os
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ API is running"

@app.route('/people')
def get_people():
    sample_people = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ]
    return jsonify(sample_people)

@app.route('/data')
def get_data():
    sample_people = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ]
    return jsonify({"data": sample_people})

# --- New fun routes ---

@app.route('/time')
def get_time():
    # Returns the current server time
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return jsonify({"current_time": now})

@app.route('/quote')
def get_quote():
    # Returns a random motivational quote
    quotes = [
        "Keep going, you’re doing great!",
        "Small steps every day lead to big results.",
        "Your future is created by what you do today.",
        "Believe you can and you’re halfway there."
    ]
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
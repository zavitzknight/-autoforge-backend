from flask import Flask, jsonify
import os

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
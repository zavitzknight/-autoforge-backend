from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# --- Database connection helper ---
def get_db_connection():
    return psycopg2.connect(
        host="localhost",      # Change if your DB is remote
        port=5432,
        database="testdb",
        user="postgres",
        password="Steph420!"   # Replace with env var in production
    )

# --- Routes ---
@app.route('/')
def home():
    return "✅ API is running"

@app.route('/people')
def get_people():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM people;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"id": r[0], "name": r[1]} for r in rows])

@app.route('/data')
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM people;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify({"data": [{"id": r[0], "name": r[1]} for r in rows]})

# --- Entry point ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="testdb",
        user="postgres",
        password="Steph420!"  # <-- replace with your actual password
    )

@app.route("/people")
def get_people():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM people;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"id": r[0], "name": r[1]} for r in rows])

if __name__ == "__main__":
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
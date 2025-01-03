import os
import psycopg2
from flask import Flask, jsonify

# Flask app
app = Flask(__name__)

# Database connection details
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "mydb")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_PORT = os.getenv("DB_PORT", "5432")

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the PostgreSQL test application!"})

@app.route("/db-test")
def db_test():
    try:
        # Connect to the database
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"status": "success", "db_version": db_version[0]})
    except Exception as e:
        return jsonify({"status": "failure", "error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

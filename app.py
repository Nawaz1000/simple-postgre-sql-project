from flask import Flask, jsonify
from db import get_users

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask + PostgreSQL!"

@app.route("/users")
def users():
    return jsonify(get_users())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


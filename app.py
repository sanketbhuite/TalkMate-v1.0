from flask import Flask, request, jsonify
from utils import get_tutor_reply

app = Flask(__name__)

@app.route("/")
def home():
    return "TalkMate API running 🚀"

@app.route("/process", methods=["GET", "POST"])
def process():
    if request.method == "GET":
        return "Use POST request 😄"
    
    user_msg = request.json["message"]
    reply = get_tutor_reply(user_msg)
    return jsonify({"reply": reply})
from flask import Flask, request, jsonify
from utils import get_tutor_reply

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
    user_msg = request.json["message"]
    result = get_tutor_reply(user_msg)
    return jsonify(result)
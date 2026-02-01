from flask import Flask, request, jsonify
from google.cloud import firestore
from datetime import datetime

app = Flask(__name__)
db = firestore.Client()


# ✅ Root URL (so the service URL works in browser)
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "ok",
        "message": "MiniRobo is running 🚀",
        "usage": {
            "endpoint": "/chat",
            "method": "POST",
            "body": {"message": "hi"}
        }
    })


# ✅ Chat endpoint
@app.route("/chat", methods=["GET", "POST"])
def chat():
    # Allow browser testing
    if request.method == "GET":
        return jsonify({
            "info": "Send a POST request with JSON",
            "example": {"message": "hello"}
        })

    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "").lower()

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    # Simple reply logic
    if "hi" in user_message or "hello" in user_message:
        bot_reply = "Hi 👋 I’m your Cloud Run bot!"
    elif "who are you" in user_message:
        bot_reply = "I’m a Python bot running on Google Cloud Run 🚀"
    else:
        bot_reply = "I heard you! I’ll get smarter soon 😊"

    # Store chat in Firestore
    db.collection("chats").add({
        "user_message": user_message,
        "bot_reply": bot_reply,
        "timestamp": datetime.utcnow()
    })

    return jsonify({"reply": bot_reply})

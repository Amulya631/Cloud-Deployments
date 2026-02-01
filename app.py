from flask import Flask, request, jsonify
from google.cloud import firestore
from datetime import datetime

app = Flask(__name__)
db = firestore.Client()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    # Simple reply logic
    if "hi" in user_message or "hello" in user_message:
        bot_reply = "Hi 👋 I’m your Cloud Run bot!"
    elif "who are you" in user_message:
        bot_reply = "I’m a Python bot running on Google Cloud Run 🚀"
    else:
        bot_reply = "I heard you! I’ll get smarter soon 😊"

    # Store in Firestore
    db.collection("chats").add({
        "user_message": user_message,
        "bot_reply": bot_reply,
        "timestamp": datetime.utcnow()
    })

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

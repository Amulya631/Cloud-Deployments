from flask import Flask, request, jsonify
from google.cloud import firestore
from datetime import datetime

app = Flask(__name__)

# Firestore client (uses Cloud Run service account)
db = firestore.Client()


# --------------------------------------------------
# Health check / Alive endpoint
# --------------------------------------------------
@app.route("/", methods=["GET"])
def health():
    return jsonify({
        "status": "MiniRobo alive 🚀"
    })


# --------------------------------------------------
# Chat endpoint
# --------------------------------------------------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "").strip().lower()

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


# --------------------------------------------------
# Local run (Cloud Run ignores this, uses gunicorn)
# --------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

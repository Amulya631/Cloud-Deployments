# 🤖 MiniRobo – Cloud Run Chatbot (Project 2)

MiniRobo is a lightweight Python-based chatbot microservice deployed on **Google Cloud Run** with **Firestore** for persistent chat storage.  
This project demonstrates building, deploying, and connecting cloud-native backend services on GCP.

---

## 🚀 Features
- REST API built using **Python (Flask)**
- Deployed as a **serverless container** on Google Cloud Run
- Stores chat conversations in **Firestore (Native mode)**
- Auto-scalable, stateless backend
- Public endpoint for testing

---

## 🛠 Tech Stack
- **Python**
- **Flask**
- **Google Cloud Run**
- **Google Firestore**
- **Buildpacks (source-based deployment)**

---

## 📁 Project Structure
project-2-chatbot/
├── app.py
├── requirements.txt
└── README.md

---

## 🔗 API Endpoints

### Health Check
```http
GET /
Response
{
  "status": "MiniRobo alive 🚀"
}
Chat Endpoint
POST /chat


Request Body

{
  "message": "hi"
}
Response

{
  "reply": "Hi 👋 I’m your Cloud Run bot!"
}
live app url
https://minirobo2-86586492757.asia-southeast1.run.app/

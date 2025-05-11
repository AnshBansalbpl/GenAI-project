# GenAI-project
# 💬 Chatbot using IBM Watson Assistant and Flask

This project is a **Conversational AI chatbot** built using **IBM Watson Assistant** and **Flask**. It provides a simple web-based interface that allows users to interact with a smart chatbot capable of understanding and responding to user queries.

## 📌 Project Overview

The aim of this project is to demonstrate how IBM Watson Assistant can be integrated into a custom Flask web application to build an intelligent chatbot. The chatbot is capable of handling conversation flows defined in Watson Assistant and provides real-time interaction through a web interface.

## 🎯 Objectives

- To integrate IBM Watson Assistant with a Flask-based backend.
- To develop a user-friendly frontend for chat interaction.
- To enable real-time, intelligent responses powered by a cloud-based AI service.
- To deploy a working chatbot prototype demonstrating practical use of GenAI in communication.

## 🧰 Technologies Used

- **Python 3**
- **Flask (Backend Web Framework)**
- **IBM Watson Assistant (Cloud-based NLP service)**
- **HTML/CSS/JavaScript (Frontend)**
- **IBM Watson SDK (`ibm-watson`)**

## 🛠️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/AnshBansalbpl/GenAI-project.git 

2. Install Required Dependencies

pip install flask ibm-watson

3. Configure IBM Watson Assistant
Update these values in your app.py file:

API_KEY = 'your-api-key'
ASSISTANT_ID = 'your-assistant-id'
URL = 'your-service-url'

4. Run the Application
python app.py

Visit http://127.0.0.1:5000 in your browser to access the chatbot interface.

🧪 Project Structure

genai-project/

├── app.py                 # Flask backend logic

├── templates/

│   └── index.html         # Frontend page

✅ Features
Real-time messaging with Watson Assistant

Session handling for each interaction

Clean and responsive chat UI

Easily extendable for more use cases

📚 References

IBM Watson Assistant Documentation

Flask Documentation

IBM Watson Python SDK

👨‍💻 Authors
Ansh Bansal

📦 License
This project is for academic purposes only.

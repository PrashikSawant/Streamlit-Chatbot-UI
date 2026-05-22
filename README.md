# 🤖 Day 10 — Streamlit Chatbot UI

A clean, multi-model AI chatbot web interface built with 
Python, Groq API, and Streamlit. The final project of the 
Foundations phase of my 30-day AI Engineering Bootcamp.

## 💡 What It Does
- Chat with AI in a clean web interface
- Switch between LLaMA models from the sidebar
- Full conversation memory across turns
- Clear chat button to reset anytime

## 🛠️ Tech Stack
- Python 3.10+
- Groq API (LLaMA 3.3 70B / LLaMA 3.1 8B)
- Streamlit — Web interface
- python-dotenv — API key management

## 🚀 Setup & Run

### 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/day10-streamlit-chatbot
cd day10-streamlit-chatbot

### 2. Install dependencies
pip install -r requirements.txt

### 3. Add your API key
Create a .env file:
GROQ_API_KEY=your_key_here

### 4. Run
streamlit run app.py

## 🧠 Key Concepts
- Streamlit session state for chat persistence
- Multi-model switching at runtime
- Chat history passed to API every turn
- Clean sidebar settings pattern

## 📁 Project Structure
day10-streamlit-chatbot/
├── app.py              # Full Streamlit UI + Groq logic
├── requirements.txt    # Dependencies
├── .env               # API key (not committed)
└── .gitignore         # Ignores .env and cache

## 🔗 Part of 30-Day AI Engineering Bootcamp
Day 10 of 30 | Foundations Phase Complete ✅

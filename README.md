# 🚀 Local AI Chat with Ollama and Streamlit

## 📋 Description

This project creates a simple web-based chat interface using Streamlit that interacts with a local AI language model served by Ollama. It allows users to send messages and receive AI-generated responses, maintaining conversation history across user inputs.

## 🛠️ Technologies Used

- Python 3  
- Streamlit — for building the web interface  
- Ollama — for running local LLM models like Llama 3  
- Requests — for making HTTP POST requests to the local Ollama API  

## ⚙️ How It Works

- 🖥️ Starts a local Ollama server with a downloaded LLM model (e.g., Llama 3).  
- 🌐 Provides a web interface where users can type messages.  
- 🔁 Maintains conversation history using Streamlit session state.  
- 📡 Sends the full conversation as context to the Ollama API via HTTP POST.  
- 🤖 Displays AI-generated responses in the chat interface.

## ✅ Setup Instructions

### 📌 Prerequisites

- Python 3 installed on your system  
- Ollama installed and running locally  

### 🧱 Environment Setup

1. Install Ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3
ollama serve
```

2. Create and activate a Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate    # Linux / MacOS
venv\Scripts\activate       # Windows
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## ▶️ Running the App
```bash
streamlit run main.py
```

## 🌐 Access

Open your browser at:
```bash
http://localhost:8501
```

### ⚠️ Important Notes

- Ollama must be running locally and serving a model (e.g., llama3) at http://localhost:11434.
- This app uses a simple prompt-building strategy by sending the entire conversation history as context to the model.
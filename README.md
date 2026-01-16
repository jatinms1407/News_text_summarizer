Text Summarization using Google Gemini LLM

A professional text summarization application that leverages a pre-trained Google Gemini LLM to summarize news articles. The project demonstrates end-to-end pipeline design, preprocessing, and deployment via a web interface using Streamlit.

🌟 Features

Summarize long news articles into concise summaries

Uses Google Gemini Flash LLM for high-quality summarization

Simple Streamlit web interface for easy interaction

Modular pipeline design for preprocessing and inference

Works with sample datasets or manual input

🧠 Model Selection

Gemini Flash is chosen because:

Optimized for fast inference

Handles long context efficiently

Produces high-quality summaries suitable for news articles

Ideal for real-time applications

This approach also abstracts away the complexity of large local model downloads and heavy GPU requirements.

📊 Dataset

The XSUM dataset from Hugging Face is used for testing and experimentation:

from datasets import load_dataset
dataset = load_dataset("xsum")


XSUM contains BBC news articles paired with human-written summaries, ideal for evaluating summarization tasks.

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/text-summarizer-llm.git
cd text-summarizer-llm

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux / Mac

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set API Key

Option 1: Environment variable (recommended)

Create .env file in the project folder:

GEMINI_API_KEY=YOUR_GEMINI_API_KEY

Or set manually in Windows PowerShell:

setx GEMINI_API_KEY "YOUR_GEMINI_API_KEY"
Restart terminal after setting.

5️⃣ Run the app
streamlit run app.py


Open the link provided by Streamlit, usually:

http://localhost:8501

🌐 Public App Link

http://192.168.1.6:8501

Access the Text Summarizer App Online

🏗️ Project Structure
text_summarizer_app/
│
├── app.py               # Streamlit web app
├── summarizer.py        # Text summarization pipeline using Gemini
├── requirements.txt     # Python dependencies
├── README.md            # This file
├── .gitignore           # Ignore venv, pycache, etc.

🛠️ Pipeline Design

The project uses a modular TextSummarizer class:

Preprocessing

Clean text (remove newlines, strip spaces)

Check minimum length

Prompt Construction

Build prompt for Gemini LLM

Inference

Call Gemini API

Receive high-quality summary

Web App Integration

Streamlit provides textbox or dataset selection

Displays generated summary

This design abstracts model complexity from the application layer.




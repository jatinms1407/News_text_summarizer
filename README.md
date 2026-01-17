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


🌐 Public App Link

https://jatinms1407-news-text-summarizer-summarizer-espdqv.streamlit.app/

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




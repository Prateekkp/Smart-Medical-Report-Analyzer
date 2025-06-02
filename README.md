# 🧠 Smart Medical Report Analyzer

**A production-ready AI-powered medical report analyzer built using Streamlit and Groq API.**

Try the live demo on Streamlit Cloud: [👉 Click here to test the app](https://smart-medical-report-analyzer.streamlit.app/)

(Note: Please wait a bit sometimes, app sleeps)


---

## Overview

Smart Medical Report Analyzer is a web application that extracts and analyzes text from medical reports (PDFs or images) using OCR and Groq's powerful LLM API. It generates insightful medical summaries and recommendations to assist healthcare professionals and patients in understanding complex medical data.

---

## Features

- Upload medical reports in PDF or image formats (PNG, JPG, JPEG).
- Extract text using OCR from PDFs and images.
- Analyze extracted medical text via Groq LLM with domain-specific prompts.
- Generate comprehensive, understandable medical summaries and practical recommendations.
- Secure API key management using Streamlit Secrets.
- Responsive and clean UI with Streamlit.

---

## Tech Stack

- **Frontend:** Streamlit (Python)
- **Backend:** Python, Groq LLM API
- **OCR:** Custom PDF and image text extraction modules
- **Deployment:** Streamlit Cloud / any cloud provider

---

## Installation & Setup

```bash
# Clone the repo
git clone https://github.com/Prateekkp/Smart-Medical-Report-Analyzer.git
cd smart-medical-report-analyzer

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

# Install dependencies
pip install -r requirements.txt

# Setup environment variables or Streamlit secrets
# Add your GROQ_API_KEY in .streamlit/secrets.toml as:
# GROQ_API_KEY = "your_api_key_here"

# Run the app locally
streamlit run ui+app/main.py

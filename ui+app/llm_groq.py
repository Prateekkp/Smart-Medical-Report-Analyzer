import requests
import streamlit as st

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_BASE_URL = "https://api.groq.com/openai/v1"  # Yeh example endpoint hai; apne docs check kar lena

def ask_groq_llm(prompt):
    url = f"{GROQ_BASE_URL}/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    system_prompt = (
        "You are an experienced and professional medical assistant specializing in clinical report analysis. "
        "Your task is to carefully analyze detailed medical reports and provide a clear, concise, and clinically relevant summary. "
        "Include key findings, differential diagnoses, and practical recommendations for further evaluation or management. "
        "Use medical terminology accurately, maintain a neutral and professional tone, "
        "and ensure the output is suitable for healthcare professionals to review."
    )
    
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

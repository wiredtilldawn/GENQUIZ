import fitz  # PyMuPDF
import google.generativeai as genai
import os
import streamlit as st

# Setup Gemini
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def extract_text_from_pdf(uploaded_file):
    text = ""
    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text

def generate_quiz(text, num_questions=5, difficulty="medium", question_type="objective"):
    prompt = f"""
    Generate {num_questions} {question_type} questions of {difficulty} difficulty based on this text:
    
    {text[:3000]}
    
    Return only the questions and options with the correct answer marked clearly.
    """
    response = model.generate_content(prompt)
    return response.text

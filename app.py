import streamlit as st
from utils import extract_text_from_pdf, generate_quiz

st.set_page_config(page_title="GenQuiz - Gemini Edition", layout="centered")

st.title("🧠 GenQuiz")
st.caption("Upload a PDF and generate a quiz using Google's Gemini AI")

uploaded_file = st.file_uploader("📄 Upload your PDF", type=["pdf"])

if uploaded_file:
    st.success("✅ PDF Uploaded Successfully!")
    
    st.subheader("🎛️ Quiz Settings")
    num_questions = st.slider("Number of Questions", 1, 10, 5)
    difficulty = st.selectbox("Difficulty", ["easy", "medium", "hard"])
    question_type = st.selectbox("Type", ["objective", "subjective"])

    if st.button("🚀 Generate Quiz"):
        with st.spinner("Generating quiz using Gemini..."):
            text = extract_text_from_pdf(uploaded_file)
            quiz = generate_quiz(text, num_questions, difficulty, question_type)
        st.markdown("### 📝 Your Quiz")
        st.markdown(quiz)

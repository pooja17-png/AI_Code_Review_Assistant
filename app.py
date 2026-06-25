import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="🤖AI Code Review Assistant",
    layout="wide"
)

st.title("AI Code Review Assistant")

language = st.selectbox(
    "Programming Language",
    ["Python", "Java","JavaScript","C++"]
)

code = st.text_area(
    "Paste your code here",
    height=350
)

if st.button("Review Code"):

    with st.spinner("Reviewing Code..."):

        prompt = f"""
        You are a senior software engineer.

        Review this {language} code.

        Provide:

        1.Bugs
        2.Security Issues.
        3.Performance Issues
        4.Code Quality Improvements
        5.Best Practices
        6.Overall Rating out of 10

        Code:
        {code}
        """

        response = model.generate_content(prompt)

        st.markdown(response.text)
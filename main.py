import streamlit as st  # for UI
import os
from dotenv import load_dotenv  # to load environment variables into the application
load_dotenv()  # loading all the environment variables

import google.generativeai as genai

# Gemini API configuration
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model
ai_model = genai.GenerativeModel('gemini-pro')

# Function to generate response from the AI model
def get_gemini_response(user_question):
    response = ai_model.generate_content(user_question)
    return response.text

# Setting up the Streamlit app
st.set_page_config(
    page_title="Gemini Q/A Application",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Setting up the header
st.header("Gemini Q/A Application")

# Input field
user_question = st.text_input("Ask a question: ")

# Submit button
if st.button("Submit"):
    bot_response = get_gemini_response(user_question)
    st.write("*User*:", user_question)
    st.write("*Bot*:", bot_response)

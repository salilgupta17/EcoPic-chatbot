from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

# ✅ Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ✅ Load Gemini model
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

# ✅ Function to get Gemini response
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# ✅ Set up Streamlit page
st.set_page_config(page_title="Health Q&A ChatBot")
st.header("ECOPIC Assistant")

# ✅ Suggestions for health-related questions
health_suggestions = [
    "How to cure fever?",
    "What are the symptoms of dengue?",
    "Home remedies for cold",
    "How to reduce body pain?",
    "What to do for a sore throat?",
    "Tips for healthy skin",
    "How to boost immunity?",
    "Is headache a sign of stress?",
    "Foods to eat during fever",
    "Natural remedies for cough"
]

# ✅ Input with suggestions (autocomplete)
user_input = st.selectbox("Ask your health question:", options=[""] + health_suggestions, key="input")
submit = st.button("Ask")

# ✅ Handle input
if submit and user_input:
    with st.spinner("Analyzing your health question..."):
        bot_response = get_gemini_response(user_input)
    st.subheader("Response")
    st.write(bot_response)

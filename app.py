import os
import openai
import streamlit as st
from dotenv import load_dotenv

# Load the OpenAI API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate content using OpenAI's GPT-3.5 or higher
def generate_text(prompt, model="gpt-3.5-turbo", max_tokens=300, temperature=0.7):
    try:
        # Ensure prompt is provided
        if not prompt:
            return "Please provide a valid prompt."

        # Using the  API structure
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature,
            n=1
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit app for AI-based content creation
st.title("Generative AI Blog Writer")

# User input for the blog topic or starting text
prompt = st.text_area("Enter a topic or starting sentence for the blog:")

# Options for text generation
max_tokens = st.slider("Max length of the response (in tokens):", min_value=50, max_value=1000, value=300)
temperature = st.slider("Creativity level (temperature):", min_value=0.0, max_value=1.0, value=0.7)

# Generate content when the button is pressed
if st.button("Generate Blog Content"):
    if prompt.strip():
        with st.spinner("Generating content..."):
            generated_text = generate_text(prompt, max_tokens=max_tokens, temperature=temperature)
            st.subheader("Generated Blog Content")
            st.write(generated_text)
    else:
        st.error("Please enter a topic or sentence to generate content.")

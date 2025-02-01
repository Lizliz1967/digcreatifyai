# streamlit_app.py - DigCreatifyAI Streamlit Deployment

import streamlit as st
from models.models import generate_text, recommend_templates  # Correct import path
from templates_recommendations import templates

# Streamlit App Title
st.title("DigCreatifyAI - Create Digital Products with AI")
st.markdown("### Where Your Digital Downloads Come to Life!")

# Sidebar Navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Generate Content", "Template Recommendations", "Preview Templates"])

# Home Page
if page == "Home":
    st.header("Welcome to DigCreatifyAI!")
    st.write("This AI-powered tool helps you generate and customize digital products effortlessly.")

# Content Generation Section
elif page == "Generate Content":
    st.header("Generate AI Content")
    prompt = st.text_area("Enter your prompt for content generation")
    if st.button("Generate Content"):
        if prompt:
            result = generate_text(prompt)
            st.subheader("Generated Content:")
            st.write(result)
        else:
            st.warning("Please enter a prompt before generating content.")

# Template Recommendation Section
elif page == "Template Recommendations":
    st.header("AI-Powered Template Recommendations")
    category = st.selectbox("Select a category", ["ebook", "printable", "design_template"])
    if st.button("Recommend Template"):
        recommendation = recommend_templates({"category": category})
        st.subheader("Recommended Template:")
        st.json(recommendation)

# Preview Templates
elif page == "Preview Templates":
    st.header("Preview Available Templates")
    if st.checkbox("Show Templates"):
        st.write(templates)

# Run the Streamlit App
if __name__ == "__main__":
    st.write("Ready to deploy on Streamlit!")

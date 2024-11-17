import frontend.streamlit as st
import requests
import json

url = "http://127.0.0.1:5000/summarize"

st.set_page_config(layout="wide")

st.title("Text Summarization")

col1, col2 = st.columns(2)


with col1:
    st.header("Original Article")
    article = st.text_area("Enter the article to summarize:", height=200)
    st.header("Summary Settings")
    slider1,slider2,slider3 = st.columns(3)
    with slider1:
        max_length = st.slider("Maximum Length of Summary", min_value=100, max_value=500, value=400)
    with slider2:
        min_length = st.slider("Minimum Length of Summary", min_value=30, max_value=200, value=50)
    with slider3:
        num_beams = st.slider("Number of Beams (for beam search)", min_value=1, max_value=10, value=4)


with col2:
    st.markdown("<h2 style='text-align: center;'>Summary</h2>", unsafe_allow_html=True)
    summary_output = st.empty()   

if st.button("Summarize"):
    if article:
        data = {
            "text": article,
            "max_length": max_length,
            "min_length": min_length,
            "num_beams": num_beams
        }

        response = requests.post(url, json=data)

        if response.status_code == 200:
            result = response.json()
            summary_output.write(result["summary"])
        else:
            summary_output.write("Error in generating summary. Please try again.")
    else:
        summary_output.write("Please enter some text to summarize.")

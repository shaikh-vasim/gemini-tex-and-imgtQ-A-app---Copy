import streamlit as st
from PIL import Image
import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Funtion to load Gemini model and Gemini pro model and get response
model = genai.GenerativeModel("gemini-pro-vision")


def get_gemini_response(input, img):
    if input != "":
        response = model.generate_content([input, img])
    else:
        response = model.generate_content(img)
    return response.text


st.set_page_config(page_icon="😊",
                   page_title="Gemini pro Q&A demo")

st.header("Gemini LLM Application")


input = st.text_input("Input:-", key="input")
img_input = st.file_uploader("Choose an images...", type=['jpg', 'jpeg', 'png'])
col1, col2 = st.columns([5, 5])

image = ""
if img_input is not None:
    image = Image.open(img_input)
    with col1:
        st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Ask the Question")

if submit:
    resp_op = get_gemini_response(input, image)
    with col2:
        st.write("The response is :-")
        st.write(resp_op)

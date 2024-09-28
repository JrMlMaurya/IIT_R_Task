import pandas as pd
import numpy as np
import streamlit as st
from streamlit import session_state as ss
from PIL import Image

from OCR import ocr

st.set_page_config(layout="wide")
cols = st.columns([0.4,0.6], gap="medium")
with cols[0]:
   # Code for column 1
    image = st.file_uploader("Upload the Image...", type=["png","jpeg"])
    if image:
        st.image(image)
        text = ocr(image)
        ocr_text = text
        st.text_area("Image Content", ocr_text)

# with cols[1]:

#     st.title("Find keywords")
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # Display chat messages from history on app rerun
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])


#     if prompt := st.chat_input("Ask ur question"):
#         st.chat_message("user").markdown(prompt)
#         st.session_state.messages.append({"role": "user", "content": prompt})

#         response = f"Your quary is: {prompt}"

#         with st.chat_message("assistant"):
#             st.markdown(response)

#         st.session_state.messages.append({"role":"assistant", "content": response})


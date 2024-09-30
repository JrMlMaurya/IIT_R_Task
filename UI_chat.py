import streamlit as st
from PIL import Image
import os

from OCR import ocr 
from LM import answer


# Initialize session state variables
if 'image_uploaded' not in st.session_state:
    st.session_state['image_uploaded'] = False  # Tracks if an image has been uploaded
if 'ocr_text' not in st.session_state:
    st.session_state['ocr_text'] = ""  # Stores OCR text result
# if 'messages' not in st.session_state:
#     st.session_state.messages = []  # Stores chat messages
if 'image_path' not in st.session_state:
    st.session_state['image_path'] = ""  # Stores the file path of the uploaded image

# Helper function to save the uploaded file
def save_uploaded_file(uploaded_file):
    try:
        if not os.path.exists("tempDir"):
            os.makedirs("tempDir")
        file_path = os.path.join("tempDir", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return file_path
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Helper function to calculate dynamic height for the text area
def calculate_text_area_height(text):
    num_lines = text.count('\n') + 1
    return min(max(100, num_lines * 25), 400)  # Min 100px, Max 400px

# Set the layout of the page to wide
st.set_page_config(layout="wide")
cols = st.columns([0.4, 0.6], gap="medium")

### Image Upload and OCR Processing - LEFT COLUMN ###
with cols[0]:
    st.header("Upload Image and OCR Processing")

    # File uploader to upload the image
    uploaded_image = st.file_uploader("Upload an Image...", type=["png", "jpeg"])

    if st.button("Process OCR"):
        # Handle file upload only if a new image is uploaded
        # if uploaded_image is not None and not st.session_state['image_uploaded']:
        if uploaded_image is not None:
            file_path = save_uploaded_file(uploaded_image)
            if file_path:
                st.session_state['ocr_text'] = ocr(file_path)
                st.session_state['image_uploaded'] = True  # Set the flag to indicate image is processed
                st.session_state['image_path'] = file_path  # Store the file path

    # Display the image and OCR result if available
    if st.session_state['image_uploaded']:

            # Display the OCR result in a text area
            text_area_height = calculate_text_area_height(st.session_state['ocr_text'])
            st.text_area("OCR Result", st.session_state['ocr_text'], height=text_area_height)

            img = Image.open(st.session_state['image_path'])
            st.image(img, caption="Uploaded Image")

with cols[1]:

    st.title("Find keywords")
    if "messages" not in st.session_state:
        st.session_state.messages = []


    if prompt := st.chat_input("Ask ur question"):
        st.chat_message("user").markdown(prompt)
        #st.session_state.messages.append({"role": "user", "content": prompt})

        response = answer(prompt,st.session_state['ocr_text'])

        with st.chat_message("assistant"):
            st.markdown(response)

        #st.session_state.messages.append({"role":"assistant", "content": response})

    # # Display chat messages from history on app re-run
    # for message in st.session_state.messages:
    #     with st.chat_message(message["role"]):
    #         st.markdown(message["content"])

# Import required libraries
import streamlit as st
import numpy as np
from PIL import Image
from FaceRecognitionModule import FaceRecognitionModule
from ImagePreprocessor import ImagePreprocessor

# Set up the Streamlit application
st.set_page_config(
    page_title='Who is Your Celebrity Look-Alike? ',
    page_icon='✨',
    layout='centered'
)

st.title('✨:rainbow[Who is Your Celebrity Look Alike?]')
st.divider()
st.write("")


@st.cache_resource
def load_and_encode_images():
    recognizer = FaceRecognitionModule(images_path='Images')
    recognizer.load_images()
    recognizer.find_encoding()
    return recognizer  

recognizer = load_and_encode_images()
preprocessor= ImagePreprocessor()

with st.sidebar:
    st.info("""
    :blue[Hey there! 👋 Upload a frontal face for better results, then click "Find My Lookalike"
            'to discover your celebrity doppelganger!] 📸🚀'
    """)
    uploaded_file = st.sidebar.file_uploader("🖼️ :green[**Upload an Image**:] ", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    try:
        input_image = Image.open(uploaded_file)

        preprocessed_image = preprocessor.preprocess_image(np.array(input_image))

        face_resized, x, y, w, h = preprocessed_image[0]

        col1, col2 = st.columns(2)
        with col1:
            st.image(face_resized, caption="Uploaded Image", use_column_width=True)

        run_recognition = st.sidebar.button('Find My Lookalike', type= 'primary', use_container_width=True)

        if run_recognition:
            recognized_image= recognizer.run_face_recognition(face_resized)
            
            with col2:
                st.image(recognized_image , caption="Celebrity Look Alike", use_column_width=True)

    except Exception as e:
        st.error('Failed to load image: ' + str(e))

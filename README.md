# Who is Your Celebrity Look-Alike?

## Description:
This repository contains a Streamlit web application that uses face recognition and image preprocessing to help users find their celebrity look-alikes. Users can upload a frontal face image, and the application will identify and display the closest matching celebrity face along with a similarity percentage.

## Key Features:

- Upload an image: Users can upload a frontal face image in common formats (jpg, png, jpeg).
- Face Detection and Preprocessing: The application uses the Haar Cascade classifier for face detection and preprocessing to enhance the quality of the input image.
- Face Recognition: It employs the face_recognition library to recognize faces in the input image and find the closest matching celebrity face.
- Display Results: The application displays the uploaded image and the celebrity look-alike in separate columns, making it easy for users to compare.

## Usage:
- Clone the repository.
- Install the required libraries using pip install -r requirements.txt.
- Run the Streamlit application using streamlit run main.py.
- Upload a frontal face image to find your celebrity look-alike.

## Note:
For optimal results, it is recommended to use high-quality frontal face images.
Celebrity images should be placed in the "Images" directory for the recognition module to work correctly.

## Requirements:

- Python 3.7 or higher
- OpenCV
- NumPy
- Pillow (PIL)
- face_recognition
- Streamlit
  
## Live Demo

You can try out the application by accessing the live demo hosted on Streamlit:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://assefadsci-human-emotion-detection-app-9guxuh.streamlit.app/)

## Credits:

The face recognition module is based on the face_recognition library.
The image preprocessing module uses Haar Cascade face detection.



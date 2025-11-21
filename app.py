import numpy as np
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import cv2
from PIL import Image
import os
import warnings

st.title("Sample Image uploader")
upload_image = st.file_uploader('Upload an image (.jpg) file: ', type=["jpg", "jpeg"])
if upload_image is not None:
    # Open the uploaded file as an image using PIL
    image = Image.open(upload_image)
    st.image(image, caption="Uploaded Image", use_container_width=True)
else:
    st.write("Please upload an image file.")

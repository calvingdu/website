# Install necessary libraries
# !pip install torch torchvision streamlit streamlit-drawable-canvas

import streamlit as st
from streamlit_drawable_canvas import st_canvas
import torch
from torchvision import models, transforms
from PIL import Image
import numpy as np
from constant import *

# Streamlit page configuration
st.set_page_config(page_title="Doodle Recognition", page_icon="✏️", layout="wide", initial_sidebar_state="collapsed")
margin_r, body, margin_l = st.columns([0.4, 3, 0.4])

# Load a pretrained EfficientNet model for image classification
model = models.efficientnet_b0(pretrained=True)
model.eval()  # Set the model to evaluation mode

# Define a transform to preprocess the input image
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

with body:
    menu()
    # Define a dictionary to map predicted class indices to doodles
    doodle_dict = {
        0: 'Cat',
        1: 'Dog',
        2: 'Apple',
        3: 'Car',
        4: 'Tree'
    }

    # Set up the Streamlit app
    st.title("What Did You Draw?")

    # Display the drawing options
    st.subheader("Try drawing one of these:")
    st.write(", ".join(doodle_dict.values()))

    # Create a canvas component for drawing
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Transparent orange
        stroke_width=10,
        stroke_color="#000000",
        background_color="#FFFFFF",
        height=400,
        width=400,
        drawing_mode="freedraw",
        key="canvas",
    )

    # If there is a drawing, process it
    if canvas_result.image_data is not None:
        # Convert the canvas image to a PIL image
        img = Image.fromarray(canvas_result.image_data.astype('uint8'), 'RGB')
        img = img.convert("RGB")
        
        # Preprocess the image for the model
        img_tensor = preprocess(img).unsqueeze(0)  # Add batch dimension

        # Make a prediction
        with torch.no_grad():
            output = model(img_tensor)
            predicted_class_idx = output.argmax(dim=1).item()

        # Map the predicted class index to a doodle
        st.write(f'You drew a: {doodle_dict.get(predicted_class_idx % len(doodle_dict), "Undetermined")}')

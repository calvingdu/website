import streamlit as st
import streamlit.components.v1 as components
from constant import *

# Set the Streamlit page configuration
st.set_page_config(page_title="Pointer Follower Animation", page_icon="🖱️", layout="centered", initial_sidebar_state='collapsed')
margin_r,body,margin_l = st.columns([0.2, 5, 0.2])

menu()
st.header("💻 Portfolio",divider='red')

# Define the HTML, CSS, and JavaScript for the animation
background_effect_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(90deg, #ff7e5f, #feb47b);
            transition: background 0.5s ease;
            overflow: hidden;
        }

        #background {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at center, #ff7e5f, #feb47b);
            transition: background 0.5s ease;
        }
    </style>
</head>
<body>
    <div id="background"></div>

    <script>
        document.addEventListener('mousemove', function(e) {
            var x = e.clientX / window.innerWidth;
            var y = e.clientY / window.innerHeight;
            var gradientX = Math.floor(x * 100);
            var gradientY = Math.floor(y * 100);
            var gradient = 'radial-gradient(circle at ' + gradientX + '% ' + gradientY + '%, #ff7e5f, #feb47b)';
            document.getElementById('background').style.background = gradient;
        });
    </script>
</body>
</html>
"""

# Render the custom HTML with Streamlit
components.html(background_effect_code, height=600)
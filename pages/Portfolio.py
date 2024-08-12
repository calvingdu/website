import streamlit as st
import streamlit.components.v1 as components
from constant import *

# page config ----------------------------------------------------------------
st.set_page_config(page_title="Portofolio", page_icon="💻 ", layout="wide",initial_sidebar_state="collapsed")
margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

with body:
   menu()

   st.header("💻 Portfolio",divider='red')
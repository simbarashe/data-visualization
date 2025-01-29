# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:23:33 2025

@author: simbasj
"""

import streamlit as st

st.title("Streamit is amazing!")

st.title("NEVER USE SPACES IN FILE AND FOLDER NAMES!")


st.write("Hello, Streamlit!")

st.header("Number selection")

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")
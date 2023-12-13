import streamlit as st
from helper import magic


start = st.button("Let's get started")

if start:
    magic.pause(1)
    st.markdown(f"<h1 style='font-size: 25px;'>Welcome to...</h1>", unsafe_allow_html=True)
    magic.pause(2)
    st.markdown(f"<h1 style='font-size: 20px;'>Identifying Conflicts of Interest in the Securities Transactions of U.S. Congressional Members</h1>", unsafe_allow_html=True)
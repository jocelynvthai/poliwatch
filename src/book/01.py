import streamlit as st
from helper import magic

@st.cache_data
def main():
    magic.pause(1)
    st.markdown(f"<h1 style='font-size: 25px;'>Problem Statement</h1>", unsafe_allow_html=True)
    magic.pause(2)
    st.markdown(f"<h1 style='font-size: 20px;'>Congress has an insider trading problem. Can the American people be sure that congressional members are acting in the best interest of the public over private investment portfolios? </h1>", unsafe_allow_html=True)

main()
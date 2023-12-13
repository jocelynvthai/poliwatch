import streamlit as st
from helper import magic

if 'start' not in st.session_state:
    st.session_state['start'] = False


start = st.button("Let's get started")

if start or st.session_state['start']:
    st.session_state['start'] = True
    st.markdown(f"<h1 style='font-size: 25px;'>Welcome to...</h1>", unsafe_allow_html=True)
    magic.pause(2)
    st.markdown(f"<h1 style='font-size: 20px;'>Identifying Conflicts of Interest in the Securities Transactions of U.S. Congressional Members</h1>", unsafe_allow_html=True)
    magic.pause(2)

    problem = st.button("Problem Statement")
    if problem: 
        st.markdown(f"<h1 style='font-size: 20px;'>Congress has an insider trading problem. Can the American people be sure that congressional members are acting in the best interest of the public over private investment portfolios? </h1>", unsafe_allow_html=True)    
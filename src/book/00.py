import streamlit as st
from helper import magic


if "do_matrix_effect" not in st.session_state:
    st.session_state["do_matrix_effect"] = False

if not st.session_state.do_matrix_effect:
    st.header("Welcome to...")
    magic.pause(1)
    st.subheader("Identifying Conflicts of Interest in the Securities Transactions of U.S. Congressional Members")  
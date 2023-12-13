import streamlit as st
from helper import magic

st.header("Welcome to...")
st.subheader("Identifying Conflicts of Interest in the Securities Transactions of U.S. Congressional Members")

if "do_matrix_effect" not in st.session_state:
    st.session_state["do_matrix_effect"] = False

if not st.session_state.do_matrix_effect:
    md = """
    Hello Neo.               
    You know why you're here.              
    It's the question that drives us, Neo. 
    It's the question that brought you here. You know the question, just as I did.
    What is the **_Confusion Matrix_**?            
    Unfortunately, no one can be told what the **_Confusion Matrix_** is. You have to learn it for yourself.
    """
    # Render line by line if first time, otherwise render whole text
    for line in md.split("\n"):
        st.markdown(line, unsafe_allow_html=True)
        magic.pause(1 * len(line) / 30) # 30 chars per second
import streamlit as st

def cta_section():
    st.header("Ready to talk to your data?")
    st.write("Create your knowledge base and start asking questions.")

    st.write("")

    if st.button("Start Building →",type="primary"):
        st.switch_page("pages/signup.py")


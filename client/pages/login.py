import streamlit as st
from constants.footer import footer

st.title("🔐 Login")
st.subheader("Enter your Login Credentials in order to continue!")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

login_btn = st.button("Login", type="primary")
if login_btn:
    st.success("Login successful!")

footer()
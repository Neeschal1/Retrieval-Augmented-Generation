import streamlit as st
from constants.footer import footer

st.title("📝 Signup")
st.subheader("New to PookieAI? Register a new account in order to begin with...")

fullname = st.text_input("Full Name", placeholder="Enter your full name")
email = st.text_input("Email", placeholder="Enter your email")
username = st.text_input("Username", placeholder="Choose a username")
gender = st.radio("Gender", ["Male", "Female", "Other"], horizontal=True)
password = st.text_input("Password", type="password", placeholder="Enter your password")
confirm_password = st.text_input("Password", type="password", placeholder="Confirm your password")
remember_me = st.checkbox("Remember me :)")

signup_btn = st.button("Signup", type="primary", use_container_width=True)
    
if signup_btn:
    st.success("Signup successful!")

st.divider()

footer()
import streamlit as st
from constants.footer import footer

st.title("🔐 Login")
st.subheader("Enter your Login Credentials in order to continue!")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

left, right = st.columns([10, 1])
with right:
    st.page_link("pages/forgotpassword.py", label="ForgotPassword")

login_btn = st.button("Login", type="primary", use_container_width=True)
if login_btn:
    st.success("Login successful!")

st.divider()

footer()
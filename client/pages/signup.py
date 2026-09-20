import streamlit as st
import requests as req
from constants.footer import footer
from env_config import Config

st.title("📝 Signup")
st.subheader("New to PookieAI? Register a new account in order to begin with...")

error_placeholder = st.empty()

fullname = st.text_input("Full Name", placeholder="Enter your full name")
email = st.text_input("Email", placeholder="Enter your email")
username = st.text_input("Username", placeholder="Choose a username")
gender = st.radio("Gender", ["male", "female", "others"], horizontal=True)
password = st.text_input("Password", type="password", placeholder="Enter your password")
confirm_password = st.text_input("Password", type="password", placeholder="Confirm your password")
remember_me = st.checkbox("Remember me :-)")

signup_btn = st.button("Signup", type="primary", use_container_width=True)

if signup_btn:
    if not fullname or not email or not username or not password or not confirm_password:
        error_placeholder.error("Fill up all the credentials!")

    elif password != confirm_password:
        error_placeholder.error("Passwords do not match.")
    
    else:
        data = {
            "fullname": fullname,
            "email": email,
            "password": password,
            "username": username,
            "gender": gender
        }
        response = req.post(f"{Config.SERVER_API_URL}/users/create-users/", json=data)
        
        if response.status_code == 201:
            st.switch_page("pages/document.py")
        else:
            issue = response.json()
            detail = issue.get("detail")

            if isinstance(detail, dict):
                message = detail.get("detail") or detail.get("message")
                
            elif isinstance(detail, list):
                message = ", ".join(
                    item.get("msg", str(item))
                    if isinstance(item, dict)
                    else str(item)
                    for item in detail
                )
                
            else:
                message = str(detail)

            error_placeholder.error(message)

st.divider()

footer()
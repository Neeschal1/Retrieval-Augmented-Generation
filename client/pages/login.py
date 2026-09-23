import streamlit as st
from constants.footer import footer
import requests as req
from env_config import Config

st.title("🔐 Login")
st.subheader("Enter your Login Credentials in order to continue!")

error_placeholder = st.empty()

email = st.text_input("Email")
password = st.text_input("Password", type="password")

left, right = st.columns([10, 1])
with right:
    st.page_link("pages/forgotpassword.py", label="ForgotPassword")

login_btn = st.button("Login", type="primary", use_container_width=True)
if login_btn:
    login_data = {
        "email": email,
        "password": password,
    }
    response = req.post(f"{Config.SERVER_API_URL}/users/login/", json=login_data)

    if response.status_code == 201:
        result = response.json()
        st.session_state["access_token"] = result["tokens"]["accessToken"]
        st.session_state["refresh_token"] = result["tokens"]["refreshToken"]
        st.switch_page("pages/document.py")
    
    if response.status_code == 409:
        data = response.json()
        error_placeholder.error(data['message'])
    else:
        error_placeholder.error("Exception occured. Try again later!")

st.divider()
footer()
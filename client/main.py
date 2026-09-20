import streamlit as st

st.set_page_config(
    page_title="PookieAI",
    page_icon="👧",
    layout="wide"
)

home_page = st.Page("pages/home.py", title="Home", icon="👧")
login_page = st.Page("pages/login.py", title="Login", icon="🔐")
signup_page = st.Page("pages/signup.py", title="Signup", icon="📝")

pg = st.navigation([
    home_page,
    login_page,
    signup_page
])

pg.run()
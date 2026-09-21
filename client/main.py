import streamlit as st

st.set_page_config(page_title="PookieAI", page_icon="👧", layout="wide")

home_page = st.Page("pages/home.py", title="Home", icon="👧")
login_page = st.Page("pages/login.py", title="Login", icon="🔐")
signup_page = st.Page("pages/signup.py", title="Signup", icon="📝")
forgot_password_page = st.Page("pages/forgotpassword.py", title="ForgotPassword", icon="🔐")
upload_document_page = st.Page("pages/document.py", title="UploadDocument", icon="📝")
conversation_page = st.Page("pages/conversation.py", title="Conversation", icon="💬")
llm_page = st.Page("pages/llm.py", title="Conversation", icon="💬")

pg = st.navigation(
    {
        "": [home_page, login_page, signup_page, forgot_password_page],
        "protected": [upload_document_page, conversation_page, llm_page],
    },
    position="top",
)

pg.run()

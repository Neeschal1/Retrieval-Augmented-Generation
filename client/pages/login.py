import streamlit as st

st.title("🔐 Login")
st.subheader("Enter your Login Credentials in order to continue!")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login", type="primary"):
    st.success("Login successful!")
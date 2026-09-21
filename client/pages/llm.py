import streamlit as st
from pypdf import PdfReader
from langchain_google_genai import ChatGoogleGenerativeAI

st.title("🧠 Upload your Google LLM API Key")
st.subheader("Provide your Google LLM API in order to communicate with your provided document.")


# Dialog Popup
@st.dialog("🧠 API Uploaded")
def success_popup():
    st.success(f"API uploaded successfully!")
    st.write("You are now ready to be processed.")
    st.info("Your API key will be used to communicate with the Google LLM and generate responses based on your document.")
    if st.button("Head me to conversation page!", type="primary", use_container_width=True):
        st.switch_page("pages/conversation.py")
        st.rerun()
        

# Check Validation of LLM API Key
def validate_api_key(api_key):
    try:
        llm_api = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)
        response = llm_api.invoke("Reply with OK.")
        return True, None
    except Exception as e:
        return False, str(e)


# API Key upload guidance Popup        
@st.dialog("🔑 How to Get a Google API Key")
def api_key_help_popup():
    st.subheader("Follow these steps:")
    st.markdown(
        """
        **1. Open Google AI Studio**: Go to Google AI Studio and sign in with your Google account.
        
        **2. Create an API Key**: Look for the **Get API key** option and create a new API key.
        
        **3. Copy your API Key**: Copy the generated API key.
        
        **4. Return to PookieAI**: Paste the API key into the **Google API** field on this page.
        
        **5. Submit the API Key**: Click **Submit API Key** to continue.
        """
    )
    st.warning("Note: Never share your API key publicly or commit it to GitHub.")
    st.link_button("Open Google AI Studio", "https://aistudio.google.com/app/apikey", type="primary", use_container_width=True)


entered_llm_api_key = st.text_input("Google API", placeholder="Enter your LLM API Key", type="password")

left, right = st.columns([1, 1])
with left:
    cant_get_llm_api_key = st.button("Can't get API Key", type="secondary", use_container_width=True)
    
with right:
    submit_llm_api_key = st.button("Submit API Key", type="primary", use_container_width=True)


if submit_llm_api_key:
    if entered_llm_api_key is None:
        st.error("Please provide your LLM API Key in order to begin with...")
    with st.spinner("Validating API key..."):
        is_valid, error = validate_api_key(entered_llm_api_key)
        if is_valid:
            success_popup()
        else:
            st.error("❌ Invalid or unusable API key.")
    
    
if cant_get_llm_api_key:
    api_key_help_popup()
    

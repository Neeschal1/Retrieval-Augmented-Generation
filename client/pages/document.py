import streamlit as st
from pypdf import PdfReader
import requests as req
from env_config import Config

token = st.session_state.get("access_token")
if token is None:
    st.switch_page("pages/login.py")
    st.rerun()

st.title("📝 Upload Document")
st.subheader("Provide your document in order to integrate AI within it.")

error_placeholder = st.empty()

@st.dialog("📄 Document Uploaded")
def document_popup(filename):
    st.success(f"{filename} uploaded successfully!")
    st.write("Your document is ready to be processed.")
    if st.button("Continue", type="primary", use_container_width=True):
        st.switch_page("pages/llm.py")
        st.rerun()


document = st.file_uploader("Upload your document", type=["pdf", "txt", "docx"])
upload_doc_btn = st.button("Upload Document", type="primary", use_container_width=True)


if upload_doc_btn:
        
    if document is None:
        st.error("Please any of your document in order to begin with...")
        
    else:
        if document:
            doc_type = None
            if document.type == "application/pdf":
                doc_type = "pdf"
                reader = PdfReader(document)
                content = ""
                for page in reader.pages:
                    content += page.extract_text() or ""

            elif document.type == "text/plain":
                doc_type = "txt"
                content = document.getvalue().decode("utf-8")

            else:
                st.warning("DOCX extraction is not implemented yet.")
                content = ""

            if content:
                data = {
                    "filename": document.name,
                    "filetype": doc_type,
                    "fullcontent": content
                }
                
                access_token = st.session_state.get("access_token")
                if not access_token:
                    st.error("You are not authenticated. Please login again.")
                    st.stop()
                bearerAuthorization = {"Authorization": f"Bearer {access_token}"}
                
                response = req.post(f"{Config.SERVER_API_URL}/document/post-new-docs/", json=data, headers=bearerAuthorization)
                
                if response.status_code == 201:
                    document_popup(document.name)
                
                else:
                    data = response.json()
                    error_placeholder.error(f"Error {response.status_code}: {response.text}")
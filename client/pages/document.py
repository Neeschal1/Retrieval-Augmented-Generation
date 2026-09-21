import streamlit as st
from pypdf import PdfReader

st.title("📝 Upload Document")
st.subheader("Provide your document in order to integrate AI within it.")


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
            if document.type == "application/pdf":
                reader = PdfReader(document)
                content = ""
                for page in reader.pages:
                    content += page.extract_text() or ""

            elif document.type == "text/plain":
                content = document.getvalue().decode("utf-8")

            else:
                st.warning("DOCX extraction is not implemented yet.")
                content = ""

            if content:
                document_popup(document.name)
                
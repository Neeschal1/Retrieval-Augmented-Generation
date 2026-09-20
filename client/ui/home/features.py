import streamlit as st

def features_section():
    st.header("Everything your knowledge needs.")
    st.write("A simple workflow for turning static documents into an interactive AI knowledge base.")
    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("📚 Knowledge Base")
        st.write("Upload your documents and build a centralizedknowledge base that your AI can understand.")
        
    with col2:
        st.subheader("🔎 Intelligent Retrieval")
        st.write("Retrieve the most relevant pieces of informationbefore generating an answer.")

    with col3:
        st.subheader("💡 Contextual Answers")
        st.write("Get responses grounded in your own documentsinstead of relying only on the model's knowledge.")
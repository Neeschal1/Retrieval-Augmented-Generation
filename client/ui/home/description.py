import streamlit as st

def description_section():
    st.caption("BUILT FOR MODERN AI APPLICATIONS")

    tech1, tech2, tech3, tech4 = st.columns(4)

    with tech1:
        st.metric("📄", "Docs", "Your data")
        
    with tech2:
        st.metric("🔍", "Retrieval", "Semantic search")

    with tech3:
        st.metric("🧠", "Context", "Relevant data")

    with tech4:
        st.metric("🤖", "Generate", "AI response")
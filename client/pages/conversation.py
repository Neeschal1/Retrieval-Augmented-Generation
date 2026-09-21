import streamlit as st
from datetime import datetime

# Session
if "conversations" not in st.session_state:
    st.session_state.conversations = {}

if "current_conversation" not in st.session_state:
    conversation_id = datetime.now().strftime("%Y%m%d%H%M%S")
    st.session_state.current_conversation = conversation_id
    st.session_state.conversations[conversation_id] = {
        "title": "New Conversation",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "messages": []
    }


# Helper function 1
def create_new_conversation():
    conversation_id = datetime.now().strftime("%Y%m%d%H%M%S%f")
    st.session_state.conversations[conversation_id] = {
        "title": "New Conversation",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "messages": []
    }
    st.session_state.current_conversation = conversation_id


# Helper function 2
def get_current_conversation():
    return st.session_state.conversations[
        st.session_state.current_conversation
    ]


# Sidebar conversation memory
with st.sidebar:
    st.title("🧠 PookieAI")
    if st.button("＋ New Conversation", type="primary", use_container_width=True):
        create_new_conversation()
        st.rerun()

    st.divider()

    st.subheader("💬 Conversations")
    conversations = st.session_state.conversations
    if not conversations:
        st.caption("No conversations yet.")

    else:
        for conversation_id, conversation in reversed(list(conversations.items())):
            title = conversation["title"]
            if title == "New Conversation":
                title = "New Conversation"

            is_current = (conversation_id== st.session_state.current_conversation)

            button_label = (
                f"👉 {title}"
                if is_current
                else f"   {title}"
            )

            if st.button(button_label, key=f"conversation_{conversation_id}", use_container_width=True):
                st.session_state.current_conversation = conversation_id
                st.rerun()


# Current Conversation
conversation = get_current_conversation()
st.title("💬 Conversation")
st.caption("Ask questions about your uploaded document.")

st.divider()


# Chat History
messages = conversation["messages"]
if not messages:
    st.info("👋 Start a conversation by asking something about your document.")
else:
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


# Chat input
user_prompt = st.chat_input("Ask something about your document...")


# User message
if user_prompt:
    # Store user message
    messages.append({
        "role": "user",
        "content": user_prompt
    })
    
    # Generate Conversation Title
    if conversation["title"] == "New Conversation":
        conversation["title"] = (
            user_prompt[:30] + "..."
            if len(user_prompt) > 30
            else user_prompt
        )
        
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_prompt)
        
    # Temporary AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ("This is a temporary response. Your RAG + Gemini response will appear here.")
            st.markdown(response)
            
    # Store AI response
    messages.append({
        "role": "assistant",
        "content": response
    })
    st.rerun()
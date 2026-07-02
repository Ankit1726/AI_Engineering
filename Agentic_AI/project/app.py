import streamlit as st
from langchain_core.messages import HumanMessage
from Agentic_Bot import chatbot

# Page Config
st.set_page_config(
    page_title="Agentic AI Chatbot",
    page_icon="🤖",
    layout="wide"
)


# CSS
st.markdown("""
<style>

.stApp{
    background:#f4f7fb;
}

.main-title{
    text-align:center;
    font-size:40px;
    font-weight:700;
    color:#1f2937;
}

.sub-title{
    text-align:center;
    color:#6b7280;
    margin-bottom:25px;
}

.block-container{
    padding-top:2rem;
    max-width:900px;
}

[data-testid="stChatInput"]{
    position:fixed;
    bottom:20px;
}

</style>
""", unsafe_allow_html=True)


# Header
st.markdown(
    "<div class='main-title'>🤖 Agentic AI Chatbot</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Powered by LangGraph + Groq + Streamlit</div>",
    unsafe_allow_html=True
)

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Thread ID for MemorySaver
CONFIG = {
    "configurable": {
        "thread_id": "thread-1"
    }
}


# Display Previous Chat
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat Input
prompt = st.chat_input("Ask me anything...")

if prompt:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant Streaming Response
    with st.chat_message("assistant"):

        # Empty container that will be updated continuously
        response_placeholder = st.empty()

        # Store complete assistant response
        full_response = ""

       
        # STREAMING
        stream = chatbot.stream(
            {
                "messages": [
                    HumanMessage(content=prompt)
                ]
            },
            config=CONFIG,
            stream_mode="messages"
        )

        # Read every streamed chunk
        for message_chunk, metadata in stream:

            # Skip empty chunks
            if not message_chunk.content:
                continue

            # Add new token/text
            full_response += message_chunk.content

            # Update same placeholder
            response_placeholder.markdown(
                full_response + "▌"
            )

        # Remove cursor after streaming completes
        response_placeholder.markdown(full_response)


    # Save Assistant Message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": full_response
        }
    )
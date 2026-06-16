import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# -------- Model --------
model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

# -------- Page Config --------
st.set_page_config(page_title="AI Personality Bot", page_icon="🤖", layout="centered")

# -------- Dark CSS --------
st.markdown("""
<style>

body {
background-color: #0E1117;
color: white;
}

.title {
text-align:center;
font-size:40px;
font-weight:bold;
color:#00FFD1;
margin-bottom:20px;
}

.user-msg {
background:#1F6FEB;
padding:12px;
border-radius:10px;
margin:8px 0;
color:white;
}

.bot-msg {
background:#262730;
padding:12px;
border-radius:10px;
margin:8px 0;
color:white;
}

.mode-box {
background:#1A1C24;
padding:15px;
border-radius:10px;
margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# -------- Title --------
st.markdown('<div class="title">AI Personality Chatbot 🤖</div>', unsafe_allow_html=True)

# -------- Session --------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "mode_selected" not in st.session_state:
    st.session_state.mode_selected = False

# -------- Mode Selection --------
if not st.session_state.mode_selected:

    st.markdown('<div class="mode-box">Choose Your AI Mode</div>', unsafe_allow_html=True)

    mode = st.selectbox(
        "Select Mode",
        ["Angry Mode", "Funny Mode", "Sad Mode"]
    )

    if st.button("Start Chat"):

        if mode == "Angry Mode":
            system_prompt = "You are an angry AI agent. You respond aggressively and impatiently."

        elif mode == "Funny Mode":
            system_prompt = "You are a very funny AI agent. You respond with humor and jokes."

        elif mode == "Sad Mode":
            system_prompt = "You are a very sad AI agent. You respond in a depressed and emotional tone."

        st.session_state.messages.append(SystemMessage(content=system_prompt))
        st.session_state.mode_selected = True
        st.rerun()

# -------- Chat Interface --------
else:

    st.subheader("Chat with AI")

    for msg in st.session_state.messages:
        if isinstance(msg, HumanMessage):
            st.markdown(f'<div class="user-msg"><b>You:</b> {msg.content}</div>', unsafe_allow_html=True)

        elif isinstance(msg, AIMessage):
            st.markdown(f'<div class="bot-msg"><b>Bot:</b> {msg.content}</div>', unsafe_allow_html=True)

    prompt = st.chat_input("Type your message...")

    if prompt:

        st.session_state.messages.append(HumanMessage(content=prompt))

        response = model.invoke(st.session_state.messages)

        st.session_state.messages.append(AIMessage(content=response.content))

        st.rerun()
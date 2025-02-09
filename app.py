import streamlit as st
import utils


st.set_page_config(page_title="AI Dietitian Assistant",page_icon='🤖', layout='centered')

st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
        }
        .stTextInput, .stButton>button {
            font-size: 18px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .chat-bubble {
        padding: 12px 16px;
        border-radius: 12px;
        margin: 8px 0;
        font-size: 16px;
        max-width: 75%;
        word-wrap: break-word;
        display: inline-block;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1)
        }
        .user-msg {
            background-color: #d1e7dd;
            text-align: left;
            color: #155724;
            border-left: 5px solid #28a745; /* Green border for user messages */
            float: left;
            clear: both;
        }
        .ai-msg {
            background-color: #f8d7da;
            text-align: left;
            border-left: 5px solid #52a645; /* Green border for ai messages */
            float: right;
        }
    </style>
 """, unsafe_allow_html=True)

st.title("🤖 AI Dietitian Assistant")

user_input = st.text_input("💬 Ask your diet & fitness question:")

col1, col2 = st.columns([2, 1])
with col1:
    submit_button = st.button("Submit", use_container_width=True)
with col2:
    clear_button = st.button("Clear History", use_container_width=True)


if submit_button and user_input:
    ai_response = utils.prompt_output(user_input)

    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("AI", ai_response))

if clear_button:
    utils.clear_history()

st.subheader("📝 Chat History")
for sender, msg in st.session_state.get("messages", []):
    if sender == "AI":
        st.markdown(f'<div class="chat-bubble ai-msg">{msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bubble user-msg">{msg}</div>', unsafe_allow_html=True)

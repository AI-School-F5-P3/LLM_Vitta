import streamlit as st


def apply_custom_styles():
    st.markdown("""
        <style>
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        .stTextInput>div>div>input {
            border-radius: 20px;
        }
        .stButton>button {
            border-radius: 20px;
            width: 100%;
        }
        .chat-message {
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            display: flex;
            flex-direction: column;
        }
        .user-message {
            background-color: #e6f3ff;
            align-self: flex-end;
        }
        .bot-message {
            background-color: #f0f0f0;
            align-self: flex-start;
        }
        </style>
    """, unsafe_allow_html=True)
import streamlit as st
import pandas as pd
from agent import process_query

st.set_page_config(page_title="Drone Operations Coordinator AI Agent")

st.title("🚁 Drone Operations Coordinator AI Agent")

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# chat input
user_input = st.chat_input("Ask something...")

if user_input:

    # store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # get agent response
    response = process_query(user_input)

    # store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

# display chat history
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        if isinstance(msg["content"], pd.DataFrame):
            st.dataframe(msg["content"])
        else:
            st.write(msg["content"])

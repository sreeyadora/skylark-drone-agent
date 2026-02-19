import streamlit as st


def metric_card(title, value):

    st.metric(title, value)


def chat_message(role, message):

    if role == "user":
        with st.chat_message("user"):
            st.write(message)

    else:
        with st.chat_message("assistant"):

            if hasattr(message, "to_dict"):
                st.dataframe(message)

            else:
                st.write(message)

import streamlit as st


def metric_card(title, value):

    st.markdown(f"""
    <div style="
        background-color:#111;
        padding:20px;
        border-radius:12px;
        text-align:center;
    ">
        <h3>{title}</h3>
        <h1 style="color:#00ffaa">{value}</h1>
    </div>
    """, unsafe_allow_html=True)



def chat_message(role, message):

    if role == "user":

        st.markdown(f"""
        <div style="background:#222;padding:10px;border-radius:10px;margin:5px">
        👤 {message}
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div style="background:#111;padding:10px;border-radius:10px;margin:5px">
        🤖 {message}
        </div>
        """, unsafe_allow_html=True)

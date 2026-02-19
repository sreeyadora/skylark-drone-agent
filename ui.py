import streamlit as st


def metric_card(title, value, icon="📊"):

    st.markdown(
        f"""
        <div style="
            padding:20px;
            border-radius:15px;
            background: linear-gradient(135deg,#1f4037,#99f2c8);
            color:white;
            text-align:center;
            font-size:20px;
        ">
            <div style="font-size:30px">{icon}</div>
            <div>{title}</div>
            <div style="font-size:32px;font-weight:bold">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def chat_message(role, text):

    if role == "user":
        color = "#1f77b4"
        align = "right"
    else:
        color = "#2ca02c"
        align = "left"

    st.markdown(
        f"""
        <div style="
            text-align:{align};
            background:{color};
            color:white;
            padding:10px;
            margin:5px;
            border-radius:10px;
        ">
        {text}
        </div>
        """,
        unsafe_allow_html=True
    )

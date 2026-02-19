import streamlit as st


def metric_card(title, value):

    st.markdown(
        f"""
        <div style="
            background-color:#111;
            padding:20px;
            border-radius:10px;
            text-align:center;
            border:1px solid #333;
        ">
            <h4>{title}</h4>
            <h2>{value}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


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

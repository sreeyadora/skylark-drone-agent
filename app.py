import streamlit as st
import pandas as pd
from sheets import load_data
from agent import DroneCoordinatorAI
from ui import metric_card, chat_message


st.set_page_config(
    page_title="Drone Coordinator Enterprise",
    layout="wide"
)


ai = DroneCoordinatorAI()

pilots, drones, missions = load_data()


# SIDEBAR
st.sidebar.title("Drone Coordinator")

page = st.sidebar.radio(

    "Navigation",

    [
        "Dashboard",
        "Pilots",
        "Drones",
        "Missions",
        "AI Assistant"
    ]
)


# DASHBOARD
if page == "Dashboard":

    st.title("📊 Enterprise Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card("Pilots", len(pilots))

    with col2:
        metric_card(
            "Available Pilots",
            len(pilots[pilots["status"] == "Available"])
        )

    with col3:
        metric_card(
            "Available Drones",
            len(drones[drones["status"] == "Available"])
        )

    with col4:
        metric_card("Missions", len(missions))



# PILOTS PAGE
elif page == "Pilots":

    st.title("👨‍✈️ Pilots")

    search = st.text_input("Search pilot")

    if search:
        pilots = pilots[pilots["name"].str.contains(search, case=False)]

    st.dataframe(pilots, use_container_width=True)



# DRONES PAGE
elif page == "Drones":

    st.title("🚁 Drones")

    st.dataframe(drones, use_container_width=True)



# MISSIONS PAGE
elif page == "Missions":

    st.title("📦 Missions")

    st.dataframe(missions, use_container_width=True)



# AI CHAT PAGE
elif page == "AI Assistant":

    st.title("🤖 AI Command Center")


    if "chat" not in st.session_state:
        st.session_state.chat = []


    query = st.chat_input("Enter command")


    if query:

        st.session_state.chat.append(("user", query))

        response = ai.process(query)

        st.session_state.chat.append(("ai", str(response)))


    for role, message in st.session_state.chat:
        chat_message(role, message)

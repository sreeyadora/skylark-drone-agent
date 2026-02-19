import streamlit as st
from sheets import load_data
from agent import DroneCoordinatorAI
from analytics import show_analytics
from ui import metric_card, chat_message


st.set_page_config(
    page_title="Drone Coordinator Enterprise",
    layout="wide"
)


ai = DroneCoordinatorAI()

pilots, drones, missions = load_data()


# SIDEBAR

st.sidebar.title("🚁 Drone Enterprise")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Analytics",
        "Pilots",
        "Drones",
        "Missions",
        "AI Assistant"
    ]
)


# DASHBOARD

if page == "Dashboard":

    st.title("Enterprise Command Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card("Pilots", len(pilots), "👨‍✈️")

    with col2:
        metric_card(
            "Available Pilots",
            len(pilots[pilots["status"] == "Available"]),
            "✅"
        )

    with col3:
        metric_card(
            "Available Drones",
            len(drones[drones["status"] == "Available"]),
            "🚁"
        )

    with col4:
        metric_card("Missions", len(missions), "📦")


# ANALYTICS

elif page == "Analytics":

    show_analytics(pilots, drones, missions)


# PILOTS

elif page == "Pilots":

    st.title("Pilot Management")

    st.dataframe(pilots, use_container_width=True)


# DRONES

elif page == "Drones":

    st.title("Drone Fleet")

    st.dataframe(drones, use_container_width=True)


# MISSIONS

elif page == "Missions":

    st.title("Mission Control")

    st.dataframe(missions, use_container_width=True)


# AI ASSISTANT

elif page == "AI Assistant":

    st.title("AI Command Center")

    if "chat" not in st.session_state:
        st.session_state.chat = []

    query = st.chat_input("Enter command")

    if query:

        st.session_state.chat.append(("user", query))

        response = ai.process(query)

        st.session_state.chat.append(("ai", str(response)))

    for role, message in st.session_state.chat:
        chat_message(role, message)

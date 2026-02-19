import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sheets import load_data
from agent import DroneCoordinatorAI
from ui import metric_card, chat_message


# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="Drone Coordinator Enterprise",
    layout="wide",
    page_icon="🚁"
)


# -------------------------
# LOAD SYSTEM
# -------------------------

ai = DroneCoordinatorAI()

pilots, drones, missions = load_data()


# -------------------------
# SIDEBAR
# -------------------------

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


# -------------------------
# DASHBOARD
# -------------------------

if page == "Dashboard":

    st.title("📊 Enterprise Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card("Total Pilots", len(pilots))

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
        metric_card(
            "Total Missions",
            len(missions)
        )

    st.divider()

    st.subheader("Recent Missions")
    st.dataframe(
        missions.tail(5),
        use_container_width=True
    )


# -------------------------
# ANALYTICS
# -------------------------

elif page == "Analytics":

    st.title("📈 Analytics")

    col1, col2 = st.columns(2)

    # Pilot status chart
    with col1:

        st.subheader("Pilot Status")

        status_counts = pilots["status"].value_counts()

        fig, ax = plt.subplots()

        ax.bar(
            status_counts.index,
            status_counts.values
        )

        ax.set_title("Pilot Availability")

        st.pyplot(fig)


    # Drone status chart
    with col2:

        st.subheader("Drone Status")

        drone_counts = drones["status"].value_counts()

        fig, ax = plt.subplots()

        ax.bar(
            drone_counts.index,
            drone_counts.values
        )

        ax.set_title("Drone Availability")

        st.pyplot(fig)


# -------------------------
# PILOTS PAGE
# -------------------------

elif page == "Pilots":

    st.title("👨‍✈️ Pilot Management")

    search = st.text_input("Search Pilot")

    filtered = pilots

    if search:

        filtered = pilots[
            pilots["name"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    st.dataframe(
        filtered,
        use_container_width=True
    )


# -------------------------
# DRONES PAGE
# -------------------------

elif page == "Drones":

    st.title("🚁 Drone Fleet")

    st.dataframe(
        drones,
        use_container_width=True
    )


# -------------------------
# MISSIONS PAGE
# -------------------------

elif page == "Missions":

    st.title("📦 Mission Control")

    st.dataframe(
        missions,
        use_container_width=True
    )


# -------------------------
# AI ASSISTANT
# -------------------------

elif page == "AI Assistant":

    st.title("🤖 AI Command Center")

    st.info(
        "Try commands like:\n"
        "- show pilots\n"
        "- show drones\n"
        "- show missions\n"
        "- recommend pilot\n"
        "- recommend drone\n"
        "- assign mission"
    )

    # Initialize chat history
    if "chat" not in st.session_state:
        st.session_state.chat = []

    # Chat input
    query = st.chat_input("Enter command")

    if query:

        st.session_state.chat.append(
            ("user", query)
        )

        response = ai.process(query)

        st.session_state.chat.append(
            ("ai", response)
        )

    # Display chat history
    for role, message in st.session_state.chat:

        if role == "user":

            chat_message(
                "user",
                message
            )

        else:

            # structured response
            if isinstance(message, dict):

                if message.get("type") == "message":

                    chat_message(
                        "ai",
                        message.get("data")
                    )

                elif message.get("type") == "table":

                    st.dataframe(
                        message.get("data"),
                        use_container_width=True
                    )

            else:

                chat_message(
                    "ai",
                    str(message)
                )

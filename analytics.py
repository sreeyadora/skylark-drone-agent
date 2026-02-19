import streamlit as st
import plotly.express as px


def show_analytics(pilots, drones, missions):

    st.subheader("Pilot Availability")

    fig = px.pie(
        pilots,
        names="status",
        title="Pilot Status"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Drone Availability")

    fig2 = px.pie(
        drones,
        names="status",
        title="Drone Status"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Mission Priority")

    fig3 = px.bar(
        missions,
        x="project_id",
        y="mission_budget_inr",
        color="priority"
    )

    st.plotly_chart(fig3, use_container_width=True)

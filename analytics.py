import streamlit as st
import plotly.express as px


def show_analytics(pilots, drones, missions):

    st.title("📊 Analytics Dashboard")

    col1, col2 = st.columns(2)

    with col1:

        fig = px.pie(
            pilots,
            names="status",
            title="Pilot Availability"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        fig2 = px.pie(
            drones,
            names="status",
            title="Drone Availability"
        )

        st.plotly_chart(fig2, use_container_width=True)

    fig3 = px.bar(
        missions,
        x="client",
        y="mission_budget_inr",
        title="Mission Revenue"
    )

    st.plotly_chart(fig3, use_container_width=True)

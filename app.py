import streamlit as st
import pandas as pd
from agent import process_query
from sheets import load_data

st.set_page_config(
    page_title="Drone Operations Coordinator AI Agent",
    layout="wide"
)

st.title("🚁 Drone Operations Coordinator AI Agent")


# LOAD DATA
pilots, drones, missions = load_data()


# DASHBOARD
st.subheader("📊 Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Pilots", len(pilots))

col2.metric(
    "Available Pilots",
    len(pilots[pilots["status"] == "Available"])
)

col3.metric(
    "Available Drones",
    len(drones[drones["status"] == "Available"])
)

col4.metric("Total Missions", len(missions))


# TABS
tab1, tab2, tab3, tab4 = st.tabs([
    "Pilots",
    "Drones",
    "Missions",
    "Search & Filter"
])


with tab1:
    st.dataframe(pilots, use_container_width=True)


with tab2:
    st.dataframe(drones, use_container_width=True)


with tab3:
    st.dataframe(missions, use_container_width=True)


with tab4:

    st.subheader("Search Pilot")

    search = st.text_input("Enter pilot name")

    if search:
        result = pilots[
            pilots["name"].str.contains(search, case=False)
        ]

        st.dataframe(result)


    st.subheader("Filter by Location")

    location = st.selectbox(
        "Location",
        pilots["location"].unique()
    )

    filtered = pilots[pilots["location"] == location]

    st.dataframe(filtered)



# COMMAND AGENT
st.subheader("🤖 AI Command Center")

st.info("""
Try commands:

show pilots  
show drones  
show missions  
assign mission  
recommend pilot  
recommend drone  
mark pilot Arjun unavailable  
mark pilot Arjun available  
""")


query = st.text_input("Enter command")


if st.button("Execute Command"):

    result = process_query(query)

    if isinstance(result, pd.DataFrame):
        st.dataframe(result)

    else:
        st.success(result)



# REFRESH BUTTON
if st.button("Refresh Data"):
    st.rerun()

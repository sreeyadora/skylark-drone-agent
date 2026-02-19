import streamlit as st
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from Streamlit secrets
creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=scope
)

client = gspread.authorize(creds)

# Open sheets
pilot_sheet = client.open("pilot_roster").sheet1
drone_sheet = client.open("drone_fleet").sheet1
mission_sheet = client.open("missions").sheet1


# Load data
def load_data():

    pilots = pd.DataFrame(pilot_sheet.get_all_records())
    drones = pd.DataFrame(drone_sheet.get_all_records())
    missions = pd.DataFrame(mission_sheet.get_all_records())

    return pilots, drones, missions


# Update pilot status
def update_pilot_status(name, status):

    try:
        cell = pilot_sheet.find(name)
        pilot_sheet.update_cell(cell.row, 7, status)
        return f"{name} marked as {status}"

    except:
        return "Pilot not found"


# Update drone status
def update_drone_status(drone_id, status):

    try:
        cell = drone_sheet.find(drone_id)
        drone_sheet.update_cell(cell.row, 5, status)
        return f"Drone {drone_id} marked as {status}"

    except:
        return "Drone not found"

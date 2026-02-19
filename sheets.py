import streamlit as st
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

# Google Sheets API scope
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from Streamlit Secrets
creds_dict = st.secrets["gcp_service_account"]

creds = Credentials.from_service_account_info(
    creds_dict,
    scopes=scope
)

# Authorize client
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
    cell = pilot_sheet.find(name)
    pilot_sheet.update_cell(cell.row, 7, status)
    return "Pilot status updated in Google Sheets"


# Update drone status
def update_drone_status(drone_id, status):
    cell = drone_sheet.find(drone_id)
    drone_sheet.update_cell(cell.row, 5, status)
    return "Drone status updated"

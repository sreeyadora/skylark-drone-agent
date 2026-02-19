import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json", scope
)

client = gspread.authorize(creds)

pilot_sheet = client.open("pilot_roster").sheet1
drone_sheet = client.open("drone_fleet").sheet1
mission_sheet = client.open("missions").sheet1


def load_data():

    pilots = pd.DataFrame(pilot_sheet.get_all_records())
    drones = pd.DataFrame(drone_sheet.get_all_records())
    missions = pd.DataFrame(mission_sheet.get_all_records())

    return pilots, drones, missions


def update_pilot_status(name, status):

    cell = pilot_sheet.find(name)

    pilot_sheet.update_cell(cell.row, 7, status)

    return "Pilot status updated in Google Sheets"


def update_drone_status(drone_id, status):

    cell = drone_sheet.find(drone_id)

    drone_sheet.update_cell(cell.row, 5, status)

    return "Drone status updated"

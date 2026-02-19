import pandas as pd
from sheets import load_data, update_pilot_status, update_drone_status

# Load latest data
def get_data():
    pilots, drones, missions = load_data()
    return pilots, drones, missions


# Show functions
def show_pilots():
    pilots, _, _ = get_data()
    return pilots


def show_drones():
    _, drones, _ = get_data()
    return drones


def show_missions():
    _, _, missions = get_data()
    return missions


# Recommend pilot based on skills & availability
def recommend_pilot():
    pilots, _, missions = get_data()

    available = pilots[pilots["status"] == "Available"]

    if available.empty:
        return "No pilots available"

    best = available.iloc[0]

    return f"""
Recommended Pilot:

Name: {best['name']}
Location: {best['location']}
Skills: {best['skills']}
Status: {best['status']}
"""


# Recommend drone based on availability
def recommend_drone():
    _, drones, _ = get_data()

    available = drones[drones["status"] == "Available"]

    if available.empty:
        return "No drones available"

    best = available.iloc[0]

    return f"""
Recommended Drone:

ID: {best['drone_id']}
Model: {best['model']}
Location: {best['location']}
Status: {best['status']}
"""


# Assign mission recommendation
def assign_mission():
    pilots, drones, missions = get_data()

    available_pilot = pilots[pilots["status"] == "Available"]
    available_drone = drones[drones["status"] == "Available"]

    if available_pilot.empty or available_drone.empty:
        return "No available pilot or drone"

    pilot = available_pilot.iloc[0]
    drone = available_drone.iloc[0]

    return f"""
Mission Assignment Recommendation:

Pilot: {pilot['name']}
Drone: {drone['model']}
Location: {pilot['location']}
"""


# Command processor
def process_query(query):

    query = query.lower()

    if "show pilots" in query:
        return show_pilots()

    elif "show drones" in query:
        return show_drones()

    elif "show missions" in query:
        return show_missions()

    elif "recommend pilot" in query:
        return recommend_pilot()

    elif "recommend drone" in query:
        return recommend_drone()

    elif "assign mission" in query:
        return assign_mission()

    elif "mark pilot" in query and "unavailable" in query:

        words = query.split()
        name = words[2]

        return update_pilot_status(name.capitalize(), "Unavailable")

    elif "mark pilot" in query and "available" in query:

        words = query.split()
        name = words[2]

        return update_pilot_status(name.capitalize(), "Available")

    else:
        return "Sorry, I didn't understand."

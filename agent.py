from sheets import load_data, update_pilot_status, update_drone_status

def process_query(query):

    pilots, drones, missions = load_data()

    query = query.lower().strip()

    # Show pilots
    if "pilot" in query and "available" in query:
        return pilots[pilots["status"] == "Available"]

    elif "show pilots" in query:
        return pilots

    # Show drones
    elif "show drones" in query or "drones" in query:
        return drones

    # Show missions
    elif "show missions" in query or "missions" in query:
        return missions

    # Update pilot
    elif "mark pilot" in query and "unavailable" in query:
        name = query.replace("mark pilot", "").replace("unavailable", "").strip()
        return update_pilot_status(name, "Unavailable")

    elif "mark pilot" in query and "available" in query:
        name = query.replace("mark pilot", "").replace("available", "").strip()
        return update_pilot_status(name, "Available")

    # Update drone
    elif "mark drone" in query and "maintenance" in query:
        drone_id = query.replace("mark drone", "").replace("maintenance", "").strip()
        return update_drone_status(drone_id, "Maintenance")

    elif "mark drone" in query and "available" in query:
        drone_id = query.replace("mark drone", "").replace("available", "").strip()
        return update_drone_status(drone_id, "Available")

    else:
        return "Sorry, I didn't understand."

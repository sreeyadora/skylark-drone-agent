from sheets import load_data, update_pilot_status, update_drone_status

def process_query(query):

    pilots, drones, missions = load_data()

    query = query.lower().strip()

    if "available pilots" in query:
        return pilots[pilots["status"] == "Available"]

    elif "show pilots" in query:
        return pilots

    elif "show drones" in query:
        return drones

    elif "show missions" in query:
        return missions

    elif query.startswith("mark pilot") and "unavailable" in query:
        name = query.split()[2]
        return update_pilot_status(name, "Unavailable")

    elif query.startswith("mark pilot") and "available" in query:
        name = query.split()[2]
        return update_pilot_status(name, "Available")

    else:
        return "Sorry, I didn't understand."

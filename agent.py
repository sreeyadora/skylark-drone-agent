from sheets import load_data, update_pilot_status, update_drone_status

pilots_df, drones_df, missions_df = load_data()


# Find available pilots
def get_available_pilots(skill=None, location=None):

    df = pilots_df

    if skill:
        df = df[df['skills'].str.contains(skill, case=False)]

    if location:
        df = df[df['location'].str.contains(location, case=False)]

    df = df[df['status'] == "Available"]

    return df


# Find available drones
def get_available_drones(location=None, weather=None):

    df = drones_df

    df = df[df['status'] == "Available"]

    if location:
        df = df[df['location'].str.contains(location, case=False)]

    if weather == "Rainy":
        df = df[df['capabilities'].str.contains("IP43")]

    return df


# Conflict detection
def detect_conflicts(pilot_name, drone_id):

    pilot = pilots_df[pilots_df['name'] == pilot_name]
    drone = drones_df[drones_df['drone_id'] == drone_id]

    if pilot.empty:
        return "Pilot not found"

    if drone.empty:
        return "Drone not found"

    if pilot.iloc[0]['status'] != "Available":
        return "Pilot not available"

    if drone.iloc[0]['status'] != "Available":
        return "Drone not available"

    return "No conflict"


# Assignment
def assign_mission(pilot_name, drone_id, mission_id):

    conflict = detect_conflicts(pilot_name, drone_id)

    if conflict != "No conflict":
        return conflict

    update_pilot_status(pilot_name, "Assigned")

    update_drone_status(drone_id, "Assigned")

    return f"Mission {mission_id} assigned successfully"


# Urgent reassignment
def urgent_reassignment(mission_id):

    mission = missions_df[missions_df['project_id'] == mission_id]

    if mission.empty:
        return "Mission not found"

    skill = mission.iloc[0]['required_skills']
    location = mission.iloc[0]['locations']

    pilot = get_available_pilots(skill, location)

    drone = get_available_drones(location)

    if pilot.empty:
        return "No pilot available"

    if drone.empty:
        return "No drone available"

    pilot_name = pilot.iloc[0]['name']
    drone_id = drone.iloc[0]['drone_id']

    assign_mission(pilot_name, drone_id, mission_id)

    return f"Urgently reassigned to Pilot {pilot_name} and Drone {drone_id}"


# Chat processor
def process_query(query):

    query = query.lower()

    if "available pilot" in query:
        result = get_available_pilots()
        return result


    elif "available drone" in query:
        result = get_available_drones()
        return result.to_string()

    elif "update pilot" in query:
        name = query.split()[-1]
        return update_pilot_status(name, "On Leave")

    elif "urgent" in query:
        mission_id = query.split()[-1]
        return urgent_reassignment(mission_id)

    elif "assign" in query:
        words = query.split()
        pilot = words[1]
        drone = words[2]
        mission = words[3]
        return assign_mission(pilot, drone, mission)

    else:
        return "Sorry, I didn't understand."

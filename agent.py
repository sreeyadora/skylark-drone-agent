from sheets import load_data, update_pilot_status, update_drone_status
import pandas as pd


class DroneCoordinatorAI:

    def __init__(self):
        self.refresh()

    def refresh(self):
        self.pilots, self.drones, self.missions = load_data()

    # SMART PILOT MATCH
    def recommend_pilot(self, required_skill=None, location=None):

        pilots = self.pilots[self.pilots["status"] == "Available"]

        if required_skill:
            pilots = pilots[pilots["skills"].str.contains(required_skill, case=False)]

        if location:
            pilots = pilots[pilots["location"] == location]

        if pilots.empty:
            return None

        return pilots.iloc[0]

    # SMART DRONE MATCH
    def recommend_drone(self, required_capability=None, location=None):

        drones = self.drones[self.drones["status"] == "Available"]

        if required_capability:
            drones = drones[drones["capabilities"].str.contains(required_capability, case=False)]

        if location:
            drones = drones[drones["location"] == location]

        if drones.empty:
            return None

        return drones.iloc[0]

    # ASSIGN MISSION
    def assign_mission(self, mission_id):

        mission = self.missions[self.missions["project_id"] == mission_id]

        if mission.empty:
            return "Mission not found"

        mission = mission.iloc[0]

        pilot = self.recommend_pilot(
            mission["required_skills"],
            mission["location"]
        )

        drone = self.recommend_drone(
            mission["required_skills"],
            mission["location"]
        )

        if pilot is None or drone is None:
            return "No suitable pilot or drone available"

        update_pilot_status(pilot["name"], "Assigned")
        update_drone_status(drone["drone_id"], "Assigned")

        self.refresh()

        return {
            "mission": mission_id,
            "pilot": pilot["name"],
            "drone": drone["drone_id"]
        }

    # COMMAND PROCESSOR
    def process(self, query):

        query = query.lower()

        if "show pilots" in query:
            return self.pilots

        if "show drones" in query:
            return self.drones

        if "show missions" in query:
            return self.missions

        if "recommend pilot" in query:
            return self.recommend_pilot()

        if "recommend drone" in query:
            return self.recommend_drone()

        if "assign mission" in query:

            parts = query.split()

            if len(parts) >= 3:
                mission_id = parts[-1].upper()
                return self.assign_mission(mission_id)

        return "Command not recognized"

import pandas as pd
from sheets import (
    load_data,
    update_pilot_status,
    update_drone_status
)


class DroneCoordinatorAI:

    def __init__(self):
        self.reload()


    # -----------------------------
    # Reload latest data
    # -----------------------------
    def reload(self):

        pilots, drones, missions = load_data()

        self.pilots = pilots
        self.drones = drones
        self.missions = missions


    # -----------------------------
    # Main command processor
    # -----------------------------
    def process(self, query):

        if not query:
            return self.msg("Empty command")

        query = query.lower().strip()

        self.reload()


        # -------------------------
        # SHOW PILOTS
        # -------------------------

        if "show pilots" in query:

            return self.table(self.pilots)


        # -------------------------
        # SHOW DRONES
        # -------------------------

        if "show drones" in query:

            return self.table(self.drones)


        # -------------------------
        # SHOW MISSIONS
        # -------------------------

        if "show missions" in query:

            return self.table(self.missions)


        # -------------------------
        # MARK PILOT UNAVAILABLE
        # -------------------------

        if "unavailable" in query and "pilot" in query or "mark" in query and "unavailable" in query:

            name = self.extract_name(query)

            if name:

                update_pilot_status(
                    name,
                    "Unavailable"
                )

                return self.msg(
                    f"Pilot '{name}' marked as Unavailable"
                )

            return self.msg("Pilot not found")


        # -------------------------
        # MARK PILOT AVAILABLE
        # -------------------------

        if "available" in query and "pilot" in query or "mark" in query and "available" in query:

            name = self.extract_name(query)

            if name:

                update_pilot_status(
                    name,
                    "Available"
                )

                return self.msg(
                    f"Pilot '{name}' marked as Available"
                )

            return self.msg("Pilot not found")


        # -------------------------
        # RECOMMEND PILOT
        # -------------------------

        if "recommend pilot" in query:

            available = self.pilots[
                self.pilots["status"].str.lower() == "available"
            ]

            if available.empty:

                return self.msg("No pilots available")

            best = available.iloc[0]

            return self.msg(
                f"Recommended Pilot: {best['name']}"
            )


        # -------------------------
        # RECOMMEND DRONE
        # -------------------------

        if "recommend drone" in query:

            available = self.drones[
                self.drones["status"].str.lower() == "available"
            ]

            if available.empty:

                return self.msg("No drones available")

            best = available.iloc[0]

            return self.msg(
                f"Recommended Drone: {best['model']}"
            )


        # -------------------------
        # ASSIGN MISSION ENGINE
        # -------------------------

        if "assign mission" in query:

            return self.assign_mission()


        # -------------------------
        # UNKNOWN COMMAND
        # -------------------------

        return self.msg("Command not recognized")


    # -----------------------------
    # Extract pilot name
    # -----------------------------

    def extract_name(self, query):

        for name in self.pilots["name"]:

            if name.lower() in query:

                return name

        return None


    # -----------------------------
    # Mission assignment engine
    # -----------------------------

    def assign_mission(self):

        available_pilots = self.pilots[
            self.pilots["status"].str.lower() == "available"
        ]

        available_drones = self.drones[
            self.drones["status"].str.lower() == "available"
        ]

        if available_pilots.empty:
            return self.msg("No pilots available")

        if available_drones.empty:
            return self.msg("No drones available")

        pilot = available_pilots.iloc[0]
        drone = available_drones.iloc[0]

        return self.msg(
            f"Mission assigned to Pilot '{pilot['name']}' using Drone '{drone['model']}'"
        )


    # -----------------------------
    # Response helpers
    # -----------------------------

    def msg(self, text):

        return {
            "type": "message",
            "data": text
        }


    def table(self, dataframe):

        return {
            "type": "table",
            "data": dataframe
        }

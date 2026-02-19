from sheets import load_data, update_pilot_status, update_drone_status


class DroneCoordinatorAI:

    def __init__(self):

        self.refresh()


    def refresh(self):

        self.pilots, self.drones, self.missions = load_data()


    def process(self, command):

        cmd = command.lower().strip()


        # SHOW PILOTS
        if "show pilots" in cmd:

            return {
                "type": "table",
                "data": self.pilots
            }


        # SHOW DRONES
        elif "show drones" in cmd:

            return {
                "type": "table",
                "data": self.drones
            }


        # SHOW MISSIONS
        elif "show missions" in cmd:

            return {
                "type": "table",
                "data": self.missions
            }


        # MARK PILOT UNAVAILABLE
        elif "mark pilot" in cmd and "unavailable" in cmd:

            name = command.split("pilot")[1].split("unavailable")[0].strip()

            success = update_pilot_status(name, "Unavailable")

            self.refresh()

            if success:
                return {
                    "type": "message",
                    "data": f"Pilot {name} marked unavailable"
                }
            else:
                return {
                    "type": "message",
                    "data": "Pilot not found"
                }


        # RECOMMEND PILOT
        elif "recommend pilot" in cmd:

            available = self.pilots[
                self.pilots["status"] == "Available"
            ]

            if len(available) == 0:

                return {
                    "type": "message",
                    "data": "No pilot available"
                }

            return {
                "type": "table",
                "data": available.head(3)
            }


        # RECOMMEND DRONE
        elif "recommend drone" in cmd:

            available = self.drones[
                self.drones["status"] == "Available"
            ]

            if len(available) == 0:

                return {
                    "type": "message",
                    "data": "No drone available"
                }

            return {
                "type": "table",
                "data": available.head(3)
            }


        else:

            return {
                "type": "message",
                "data": "Command not recognized"
            }

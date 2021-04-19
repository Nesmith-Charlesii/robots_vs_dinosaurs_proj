class Fleet:

    # instead of creating fleets in main file, append
    def __init__(self):
        self.fleet_name = " "
        self.fleet_array = []

    def add_to_fleet(self, robot):
        # Todo: Remove robot from array if health is 0
        self.fleet_array.append(robot.name)
        return f"{robot.name} has been added to {self.fleet_name}\n******"

    def fleet_stats(self):
        print(f"fleet name: {self.fleet_name}\nfleet array: {self.fleet_array}\n******")

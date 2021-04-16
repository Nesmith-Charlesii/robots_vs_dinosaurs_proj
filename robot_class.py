class Robot:
    def __init__(self):
        self.name = " "
        self.health = 100
        self.power_level = 80
        self.weapon_type = "no weapon yet"
        self.attack_power = 65

    def robot_stats(self):
        print(f"name: {self.name}\nhealth: {self.health}\npower level: {self.power_level}\nweapon type: {self.weapon_type}\nattack power: {self.attack_power}\n******")

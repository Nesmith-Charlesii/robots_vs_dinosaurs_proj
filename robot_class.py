import random

class Robot:
    def __init__(self):
        self.name = " "
        self.health = 100
        self.power_level = 80
        # underscore denotes a protected property - read-only
        self._weapon = " "

    def robot_stats(self):
        print(f"name: {self.name}\nhealth: {self.health}\npower level: {self.power_level}\nweapon: {self._weapon}\n******")

    #  attain weapon takes a weapon object
    def attain_weapon(self, weapon):
        self._weapon = weapon._weapon
        print(f"{self.name} has attained the {self._weapon}")
        pass

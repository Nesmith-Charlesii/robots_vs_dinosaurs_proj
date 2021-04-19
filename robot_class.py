import random
# You can import a weapon from the weapon class and assign it to the self._weapon attribute

class Robot:
    def __init__(self):
        self.name = " "
        self._health = 100
        self._power_level = 80
        # underscore denotes a protected property - read-only
        self._weapon = "no weapon yet"
        self._attack_power = 'none'

    # display a robot's full stats. must call to view protected properties
    def robot_stats(self):
        return f"name: {self.name}\nhealth: {self._health}\npower level: {self._power_level}\nweapon: {self._weapon}\nattack power: {self._attack_power}\n******"

    #  attain_weapon method takes a weapon object. The weapon object's attack power is then assigned to the robot's attack_power.
    def attain_weapon(self, weapon):
        self._weapon = weapon._weapon
        self._attack_power = weapon._attack_power
        return f"{self.name} has attained the {self._weapon}\nattack power: {self._attack_power}\n******"

    def attack(self, dinosaur):
        # check if dinosaur is already destroyed
        if dinosaur._health < 0:
            return "dinosaur either no longer exists or has already been destroyed"
        # check if power level is depleted
        if self._power_level <= 0:
            return f"robot power level: {self._power_level}\nRobot power level depleted. Recharge!"
        # display target info to verify the correct hit
        print(f"Target:\n\tdinosaur type: {dinosaur.type}\n\tdinosaur health: {dinosaur._health}\n******")
        dinosaur._health -= self._attack_power
        self._power_level -= 10
        if dinosaur._health <= 0:
            return "This dinosaur has been destroyed"
        return f"{self.name} has successfully attacked a {dinosaur.type}.\ndinosaur health: {dinosaur._health}\n******"
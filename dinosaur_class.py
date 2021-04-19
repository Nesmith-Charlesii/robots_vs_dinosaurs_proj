
class Dinosaur:
    def __init__(self):
        self.type = "no type yet"
        self._health = 100
        self._energy = 75
        self._attack_power = 35

    def dinosaur_stats(self):
        print(
            f"type: {self.type}\nhealth: {self._health}\nenergy: {self._energy}\nattack power: {self._attack_power}\n******")

    def attack(self, robot):
        # check if robot is already destroyed
        if robot._health <= 0:
            return "robot either no longer exists or has already been destroyed"
        # check if energy level is depleted
        if self._energy <= 0:
            return "Dinosaur energy depleted. This dinosaur must 'rest()'"
        print(f"Target:\n\trobot name: {robot.name}\n\trobot health: {robot._health}\n******")
        robot._health -= self._attack_power
        self._energy -= 10
        if robot._health <= 0:
            print(f"robot {robot.name}  has been destroyed")
        return f"{self.type} has successfully attacked robot {robot.name}.\nrobot health: {robot._health}\n******"

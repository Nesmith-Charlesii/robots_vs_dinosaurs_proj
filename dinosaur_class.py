class Dinosaur:
    def __init__(self):
        self.type = "no type yet"
        self.health = 100
        self.energy = 75
        self.attack_power = 55

    def dinosaur_stats(self):
        print(f"type: {self.type}\nhealth: {self.health}\nenergy: {self.energy}\nattack power: {self.attack_power}\n******")
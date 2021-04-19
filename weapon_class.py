import random


class Weapon:
    def __init__(self):
        # protected property. read-only. cannot change unless generate weapon method is called
        self._weapon = "no weapon yet"
        self._attack_power = "none"

    def generate_weapon(self):
        weapon_list = ['plasma gun', 'rocket launcher', '50 cal', 'kamikaze']
        rand = random.randrange(0, 3)
        generated_weapon = weapon_list[rand]
        self._attack_power = random.randrange(25, 70)
        self._weapon = generated_weapon
        print(f"generated weapon: {self._weapon}\nattack power: {self._attack_power}\n******")

    def display_weapon(self):
        print(f"Weapon: {self._weapon}\nattack power: {self._attack_power}\n******")

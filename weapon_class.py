import random


class Weapon:
    def __init__(self):
        self._weapon = "no weapon yet"

    def generate_weapon(self):
        weapon_list = ['plasma gun', 'rocket launcher', '50 cal', 'kamikaze']
        rand = random.randrange(0, 3)
        generated_weapon = weapon_list[rand]
        self._weapon = generated_weapon
        print(f"generated {self._weapon}")

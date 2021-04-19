import random
from fleet_class import Fleet
from herd_class import Herd


class Battlefield:
    def __init__(self, fleet, herd):
        user_choice = input("Create a battlefield location or type 'generate' for a random selection:  ")
        if user_choice == 'generate':
            battlefield_list = ['2098 jurassic park', 'prehistoric terrain', 'modern day new york',
                                'onsite devCodeCamp']
            rand = random.randrange(0, 3)
            self.battlefield_location = battlefield_list[rand]
        else:
            self.battlefield_location = user_choice
        self.fleet = fleet()
        self.herd = herd()

    def run_game(self):
        # while len(self.fleet.fleet_array) < 0 or len(self.herd.herd_array) < 0:
        #     print("Game over")
        #     break
        self.display_welcome()
        self.battle()
        self.display_winner()

    def display_welcome(self):
        pass

    def battle(self):
        # while len(self.herd.herd_array) > 0 and len(self.fleet.fleet_array) > 0:
        # robot = self.robo_turn()
        # dinosaur = self.dino_turn()
        # robot.attack(dinosaur)
        # dinosaur.attack(robot)
        pass

    def dino_turn(self):
        pass

    def robo_turn(self):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winner(self):
        pass

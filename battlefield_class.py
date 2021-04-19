import random

class Battlefield:
    def __init__(self):
        self.battlefield_location =
        self.fleets = []
        self.herds = []

    def set_battlefield(self):
        battlefield_list = ['2098 jurassic park', 'prehistoric terrain', 'modern day new york', 'onsite devCodeCamp']
        rand = random.randrange(0, 3)
        self.battlefield_location = battlefield_list[rand]
        return self.battlefield_location

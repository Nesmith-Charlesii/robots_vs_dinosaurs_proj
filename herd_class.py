class Herd:
    def __init__(self):
        self.herd_name = " "
        self.herd_array = []

    # use the * symbol and a parameter name for unlimited parameters
    def add_to_herd(self, *args):
        # for loop through the tuple of args
        for dino in args:
            self.herd_array.append(dino.type)
            return f"A {dino.type} has been added to herd {self.herd_name}\n******"

    def herd_stats(self):
        print(f"herd name: {self.herd_name}\nherd array: {self.herd_array}\n******")

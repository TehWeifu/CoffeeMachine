# our class Ship
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self, destiny):
        print("The {} has sailed for {}!".format(self.name, destiny))


destination = input()
black_pearl = Ship("Black Pearl", 800)
black_pearl.sail(destination)

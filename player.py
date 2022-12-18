from node import node
class player:
    def __init__(self, color, pos, resources):
        self.color = color
        self.pos = pos
        self.resources = resources
    
    def print_resources(self):
        print("Here is player", self.color, "at point", self.pos.number, ".")
        print(self.resources[0], self.resources[1], self.resources[2])

    def move(self, pos, transport):
        self.resources[index] = self.resources[index] - 1
        self.pos.occupied = 0;
        self.pos = pos
        self.pos.occupied = 1;
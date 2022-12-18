from node import node
class player:
    def __init__(self, color, pos, resources):
        self.color = color
        self.pos = pos
        self.resources = resources
    
    def print_resources(self):
        print("The", self.color, "player is at point", str(self.pos.number) + ".")
        print("They have", self.resources[0], "taxi tickets,", self.resources[1], "bus tickets and", self.resources[2], "underground tickets.")

    def move(self, pos, transport):
        self.resources[transport] = self.resources[transport] - 1
        self.pos.occupied = 0;
        self.pos = pos
        self.pos.occupied = 1;

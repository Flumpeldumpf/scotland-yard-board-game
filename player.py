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
        index = 0
        if transport == 2:
            index = 0
        elif transport == 3:
            index = 1
        elif transport == 5:
            index = 2
        if pos.occupied == 0:
            if self.resources[index] > 0:
                if self.pos.check_connectivity(pos) % transport == 0 and transport > 1:
                    self.resources[index] = self.resources[index] - 1
                    self.pos.occupied = 0;
                    self.pos = pos
                    self.pos.occupied = 1;
                    return("Move successful!")
                else:
                    return("Your method of transportation does not connect to this node.")
            else:
                return("You are out of tokens for this type of transport.")
        else:
            return("Node is already occupied");

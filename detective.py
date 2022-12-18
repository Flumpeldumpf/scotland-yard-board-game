from node import node
class detective:
    def __init__(self, color, pos, resources):
        self.color = color
        self.pos = pos
        self.resources = resources
    
    def print_resources(self):
        print(self.resources[0], self.resources[1], self.resources[2])

    def move(self, pos, transport):
        if pos.occupied == 0:
            if self.resources[transport] > 0:
                if self.pos.check_connectivity(pos) % transport == 0:
                    self.resources[transport] = self.resources[transport] - 1
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

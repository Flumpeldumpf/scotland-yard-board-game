from node import node
class detective:
    def __init__(self, color, pos, resources):
        self.color = color
        self.pos = pos
        self.resources = resources

    def move(self, pos, transport):
        if self.resources[transport] > 0:
            if self.pos.check_connectivity(pos) % transport == 0:
                self.resources[transport] = self.resources[transport] - 1
                self.pos = pos
                return("Move successful!")
            else:
                return("Your method of transportation does not connect to this node.")
        else:
            return("You are out of tokens for this type of transport.")

class detective:
    def __init__(self, color, pos, resources):
        self.color = color
        self.pos = pos
        self.resources = resources
    def move(self, pos, transport):
        if self.resources[transport] > 0:
            self.resources[transport]--;
        else
            return("You are out of tokens for this type of transport.")
        #check isConnected here
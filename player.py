from node import nodeplayer_list
class player:
    def __init__(self, color, pos, resources):
        self.color = color
        self.pos = pos
        self.resources = resources
    
    def print_resources(self):
        print("The", self.color, "player is at point", str(self.pos.number) + ".")
        print("They have", self.resources[0], "taxi tickets,", self.resources[1], "bus tickets and", self.resources[2], "underground tickets.")

    def move(self, misterx, pos, transport):
        self.resources[transport] = self.resources[transport] - 1
        misterx.resources[transport] = misterx.resources[transport] + 1
        self.pos.occupied = 0;
        self.pos = pos
        self.pos.occupied = 1;

class mrx(player):
    
    def print_resources(self, round):
        print("Round:", round)
        if(round not in [3, 8, 13, 18, 24]):
            print("Mr. X is hidden")
        else:
            print("Mr. X is at point", str(player.pos.number) + ".")
        print("They have", player.resources[0], "taxi tickets,", splayerresources[1], "bus tickets", player.resources[2], "underground tickets,",
        player.resources[3], "Mr. X tickets and", player.resources[4], "double move tickets.")

    def move(self, pos, transport):
        player.resources[transport] = player.resources[transport] - 1
        player.pos.occupied = 0
        player.pos = pos
        player.pos.occupied = 2

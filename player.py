from node import node

class player:
    def __init__(self, color, pos, resources):
        self.color = color
        self.pos = pos
        self.resources = resources
    
    def print_resources(self, round, double):
        print("The", self.color, "player is at point", str(self.pos.number) + ".")
        print("They have", self.resources[0], "taxi ticket(s),", self.resources[1], "bus ticket(s) and", self.resources[2], "underground ticket(s).")

    def move(self, pos, misterx, transport, trstr):
        self.resources[transport] = self.resources[transport] - 1
        misterx.resources[transport] = misterx.resources[transport] + 1
        print("(Mr.X recieves 1", trstr + ".)")
        self.pos.occupied = False
        self.pos = pos
        self.pos.occupied = True
        print("The", self.color, "player is now at", str(self.pos.number)+".\n")
#Mr. X player subclass
class mrx(player):

    def __init__(self, color, pos, resources):
        self.color = color
        self.pos = pos
        self.resources = resources
    
    def print_resources(self, round, double):
        print("Round:", round + double)
        if(double == 1):
            self.resources[4] = 1
        if(double == 2):
            self.resources[4] = 0       
        if((round + double) not in [3, 8, 13, 18, 24]):
            print("Mr. X is hidden. ---", str(self.pos.number) + " ---")
        else:
            print("Mr. X is at point", str(self.pos.number) + ".")
        print("They have", self.resources[0], "taxi ticket(s),", self.resources[1], "bus ticket(s)", self.resources[2], "underground ticket(s),", self.resources[3], "Mr. X ticket(s) and", self.resources[4], "double move ticket(s).")

    def move(self, pos, misterx, transport, trstr):
        if(transport == 3):
            print("Mr. X used a Mr. X ticket!")
        else:
            print("Mr. X used a", trstr, "ticket.")
        self.resources[transport] = self.resources[transport] - 1
        self.pos.occupied = False
        self.pos = pos
        self.pos.occupied = True

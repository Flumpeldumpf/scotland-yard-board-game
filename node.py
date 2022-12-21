#Defines one of the 199 places on the map.
#number 
class node:
    def __init__(self, number, taxi, bus, metro):
        self.number = int(number)
        self.taxi = taxi.split(",")
        self.bus = bus.split(",")
        self.metro = metro.split(",")
        self.occupied = 0

    # def __str__(self):
    #     print(str(self.number))
    def returnsmth(self):
        return self.number

    def check_connectivity(self, node):
        retval = 1;
        if self.taxi.count(str(node.number)) > 0:
            retval *= 2
        if self.bus.count(str(node.number)) > 0:
            retval *= 3
        if self.metro.count(str(node.number)) > 0:
            retval *= 5
        return retval


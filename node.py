class node:
    def __init__(self, number, taxi, bus, metro):
        self.number = number
        self.taxi = taxi.split(",")
        self.bus = bus.split(",")
        self.metro = metro.split(",")
        self.occupied = false

    # def __str__(self):
    #     print(str(self.number))
    def returnsmth(self):
        return self.number
    def check_connectivity(self, node):
        retval = 1;
        if self.taxi.count(node.number) > 0:
            retval *= 2
        if self.bus.count(node.number) > 0:
            retval *= 3
        if self.metro.count(node.number) > 0:
            retval *= 5
        return retval


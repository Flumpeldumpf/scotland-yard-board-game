class node:
    def __init__(self, number, taxi, bus, metro):
        self.number = number
        self.taxi = taxi.split(",")
        self.bus = bus.split(",")
        self.metro = metro.split(",")

    # def __str__(self):
    #     print(str(self.number))
    def returnsmth(self):
        return self.number
    def check_connectivity(self, node):
        retval = 0;
        if self.taxi.count(node) > 0:
            retval += 100
        if self.bus.count(node) > 0:
            retval += 10
        if self.metro.count(node) > 0:
            retval += 1
        return retval


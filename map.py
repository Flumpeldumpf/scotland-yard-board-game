class map:
    def __init__(self, node_list, ):
        self.node_list = node_list

    def makemap():
        f = open("connections.txt", "r")
        
        line = f.readline()
        while line:
            list = line.split(" ")
            node(list[0], list)

        f.close()
from node import node

class map:
    def __init__(self, node_list):
        self.node_list = node_list

    def makemap(self):
        f = open("scotland_yard.txt", "r")
        
        line = f.readline()
        while line:

            list = line.split(" ")
            list[3] = list[3].split("\n")[0]
            n = node(list[0], list[1], list[2], list[3])
            self.node_list.append(n)
            line = f.readline()

        f.close()

    def return_map(self):
        for i in range(len(self.node_list)):
            print(self.node_list[i].returnsmth())

    def find_shortest_route(self, node1, node2):
        temp_node_list = [node1]
        final_node_list = []
        links_needed = 0
        while node2 not in temp_node_list:
            links_needed += 1
            for node in temp_node_list:
                for neighbor in node.taxi:

                    if node.taxi not in temp_node_list:
                        temp_node_list.append(node.taxi)

    
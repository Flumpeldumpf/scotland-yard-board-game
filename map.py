from node import node
import networkx as nx

class map:
    def __init__(self, node_list):
        self.node_list = node_list
        self.taxis = nx.Graph()
        self.buses = nx.Graph()
        self.metros = nx.Graph()

    def makemap(self):
        self.taxis.add_nodes_from(range(1,200))
        self.buses.add_nodes_from(range(1,200))
        self.metros.add_nodes_from(range(1,200))

        f = open("scotland_yard.txt", "r")
        
        line = f.readline()
        while line:

            list = line.split(" ")
            list[3] = list[3].split("\n")[0]
            n = node(list[0], list[1], list[2], list[3])
            self.node_list.append(n)
            for i in list[1].split(","):
                if (i != 0):
                    self.taxis.add_edge(int(list[0]), int(i))
            for i in list[2].split(","):
                if (i != 0):
                    self.buses.add_edge(int(list[0]), int(i))
            for i in list[3].split(","):
                if (i != 0):
                    self.metros.add_edge(int(list[0]), int(i))

            line = f.readline()

        f.close()

    def return_map(self):
        for i in range(len(self.node_list)):
            print(self.node_list[i].returnsmth())

    def find_shortest_route(self, node1:node, node2:node):
        temp_node_list = [node1]
        temp_node_list_two = []
        visited = []
        links_needed = 0
        while node2 not in temp_node_list:
            links_needed += 1
            #looks at all of the neighbours in temp_node_list
            for n in temp_node_list:

                if n not in visited:
                    for neighbor in n.taxi:

                        if self.node_list[int(neighbor) -1] not in temp_node_list + stale_node_list:
                            temp_node_list_two.append(self.node_list[int(neighbor) -1])

            visited.extend(temp_node_list_two)
            temp_node_list = temp_node_list_two
            temp_node_list_two = []
        return links_needed

    
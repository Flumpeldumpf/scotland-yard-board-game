from node import node
import networkx as nx
#import matplotlib.pyplot as plt

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
        #taxis = nx.petersen_graph()
        f.close()

    def return_map(self):
        for i in range(len(self.node_list)):
            print(self.node_list[i].returnsmth())

    def find_shortest_route(self, node1:node, node2:node):

        queue = []
        cost = 200
        pred=[-1 for i in range(200)]
        dist=[200 for i in range(200)]
        visited = [False for i in range(200)]

        visited[node1.number] = True
        dist[node1.number] = 0
        queue.append(node1)

        while(len(queue) != 0):
            u = queue[0]
            queue.pop(0)
            for i in u.taxi:
                j = self.node_list[int(i)].number
                if visited[j] == False:
                    visited[j] = True
                    dist[j] = dist[u.number] + 1
                    pred[j] = u.number
                    queue.append(self.node_list[int(i)])

                    if j == node2.number:
                        path = [node2]
                        crawl = node2;
        
                        while (pred[crawl.number] != -1):
                            print(crawl.number)
                            path.append(pred[crawl.number]);
                            crawl = self.node_list[pred[crawl.number]];
                        return len(path)

    
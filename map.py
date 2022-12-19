from node import node
import networkx as nx
import matplotlib.pyplot as plt
from player import player

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
        #nx.draw(self.taxis, with_labels=1)
        #plt.show()
    
    def print_player_locations(self, players):
        for player in players:
            print("The", player.color, "player is at point", str(player.pos.number)+".")
        print("Mr. X is at point ????.")


    def return_map(self):
        for i in range(len(self.node_list)):
            print(self.node_list[i].returnsmth())

    def find_shortest_route(self, node1:node, node2:node):

        queue = []
        cost = 200
        pred=[-1 for i in range(199)]
        dist=[200 for i in range(199)]
        visited = [False for i in range(199)]

        visited[node1.number -1] = True
        dist[node1.number -1] = 0
        queue.append(node1)

        while(len(queue) != 0):
            u = queue[0]
            queue.pop(0)
            #print(u.taxi)
            for i in u.taxi:
                #print(self.node_list[int(i) -1].number)
                j = self.node_list[int(i) -1].number
                if visited[j-1] == False:
                    visited[j-1] = True
                    dist[j-1] = dist[u.number -1] +1
                    #print(u.number)
                    pred[j-1] = u.number
                    queue.append(self.node_list[int(i) -1])


                    if j == node2.number:
                        #print(pred)
                        #print(visited)
                        #print(dist)
                        path = [node2.number]
                        crawl = pred[node2.number -1]
                        
                        while (crawl != -1):
                            
                            path.append(crawl)
                            crawl = pred[self.node_list[crawl-1].number -1]
                            #print(crawl)
                            #print(pred[crawl.number -1])
                        return path
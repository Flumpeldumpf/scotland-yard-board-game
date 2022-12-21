import random
from map import map

class setup:
    def __init__(self, doubleuses):
        self.doubleuses = doubleuses
    
    def start_of_game(self):
        print("-----SCOTLAND YARD-----")
        print("-----hunting mr. x-----")
        print("                       ")
        input("Press Enter To Continue...")

    #Handles turns for all players and Mr. X
    #player => the player object that is moving
    def take_turn(self, player, misterx, map, round):
        d = player
        n = player.pos
        m = map
        if(round + self.doubleuses == 25):
            return 1
        player.print_resources((round + self.doubleuses), self.doubleuses)
        foundmrx = self.get_input_move(misterx, d,n,m)
        if foundmrx == 1:
            return 2
        if(misterx == player):
            if player.resources[4] != 0:
                print("would you like to use a double move? (yes or no)")
                answer = input()
                if(answer == "yes"):
                    self.doubleuses = self.doubleuses + 1
                    if(round + self.doubleuses == 25):
                        return 1
                    player.print_resources(round, self.doubleuses)
                    self.get_input_move(misterx, d,n,m)
        return 0          



    def get_input_move(self, misterx, player, node, map):
        d = player
        n = node
        m = map
        trans_input = ""
        index = -1

        if (player.resources[0] == 0 and player.pos.bus == ['0']) or (player.resources[1] == 0 and player.pos.metro == ['0']):
            print("sorry bub! you can't move buddy. ha.")
            return 0
        else:
            #Gets a legal move
            valid = False
            while not valid:
                print("Input the point you would like to move to.")
                target = input()
                
                #Checks if point is valid
                if target.isnumeric():
                    target = int(target)
                    if (target > 0) and (target < 200):

                        multiple = n.check_connectivity(map.node_list[target-1])
                        if multiple != 1:

                            #Checks if point is occupied
                            #print(map.node_list[target - 1].occupied)
                            if map.node_list[target-1].occupied == False:
                                

                                validtwo = False
                                while not validtwo:        

                                    #Resolves if there are multiple ways to travel somewhere
                                    if multiple != 7 and multiple >= 6:
                                        print("Input your method of transportation.")
                                        
                                        trans_input = input()
                                        transport = 1
                                        if trans_input == "taxi":
                                            transport = 2
                                            validtwo = True
                                            index = 0
                                        elif trans_input == "bus":
                                            transport = 3
                                            validtwo = True
                                            index = 1
                                        elif trans_input == "underground":
                                            transport = 5
                                            validtwo = True
                                            index = 2
                                        elif trans_input == "water":
                                            transport = 7
                                            validtwo = True
                                            index = 3
                                        else:
                                            print("This type of transportation does not exist. Please enter taxi, bus, or underground.")
                                            validtwo = False
                                            continue
                                        if multiple % transport != 0:
                                            print("This method of transportation is not possible.")
                                            validtwo = False
                                            continue
                                    else:
                                        if multiple == 2:
                                            index = 0
                                            validtwo = 1
                                            trans_input = "taxi"
                                        elif multiple == 3:
                                            index = 1
                                            validtwo = 1
                                            trans_input = "bus"
                                        elif multiple == 5:
                                            index = 2
                                            validtwo = 1
                                            trans_input = "underground"
                                        else :
                                            index = 3
                                            validtwo = 1
                                            trans_input = "water"
                                        if multiple % transport != 0:
                                            print("This method of transportation is not possible.")
                                            validtwo = False
                                            continue
                                
                                        
                                #Checks if there are resourses for chosen type of transportation
                                if d.resources[index] > 0:
                                    valid = True
                                else:
                                    print("You do not have enough resources for this mode of transportation.")
                                    continue

                            #Checks if node is occupied by Mr. X
                            elif map.node_list[target - 1].occupied is True and misterx.pos.number == d.pos.number:
                                return 1
                            else:
                                print("This node is occupied.")
                                continue
                        else:
                            print("There is no connection to this node.")
                            continue
                    else:
                        print("This is not a valid point number.")
                        continue
                else:
                    print("This is not a valid point number.")
                    continue

            if(d == misterx) and (misterx.resources[3] != 0) and trans_input != "water":
                print("Would you like to use a Mr. X ticket? (yes or no)")
                ans = input()
                if(ans == "yes"):
                    index = 3
    
            d.move(m.node_list[target-1], misterx, index, trans_input)
            return 0

    def generate_start_positions(self):
        possible_sp = [13, 26, 29, 34, 50, 53, 91, 94,
         103, 112, 117, 132, 138, 141, 155, 174, 197, 198]
        
        x = 0
        sps = []
        sp = 0
        while(x != 5):
            sp = possible_sp[random.randint(0,17)]
            if sp not in sps:
                sps.append(sp)
                x += 1
        return sps
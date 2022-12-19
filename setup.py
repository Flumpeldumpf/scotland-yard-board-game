import random
from map import map

class setup:
    def __init__(self, doubleuses):
        self.doubleuses = doubleuses
    
    def start_of_game(self):
        self.doubleuses = 0
        print("-----SCOTLAND YARD-----")
        print("-----hunting mr. x-----")
        print("                       ")
        input("Press Enter To Continue...")

    def take_turn(self, misterx, player, map, round):
        d = player
        n = player.pos
        m = map
        if(round + self.doubleuses == 25):
            return 1
        player.print_resources(round + self.doubleuses)
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
                    player.print_resources(round + self.doubleuses)
                    self.get_input_move(misterx, d,n,m)
        return 0          



    def get_input_move(self, misterx, player, node, map):
        d = player
        n = node
        m = map
        
        if (player.resources[0] == 0 and player.pos.bus == ['0']) or (player.resources[1] == 0 and player.pos.metro == ['0']):
            print("sorry bub! you can't move buddy. ha.")
            return 0
        else:
            valid = False
            while not valid:
                print("Input the point you would like to move to.")
                target = input()
                if target.isnumeric():
                    target = int(target)
                    if (target > 0) and (target < 200):
                        if map.node_list[target - 1].occupied == 0:
                            multiple = n.check_connectivity(map.node_list[target-1])
                            if multiple >= 6:
                                print("Input your method of transportation.")
                                transport = 1
                                trans_input = input()
                                if trans_input == "taxi":
                                    transport = 2
                                elif trans_input == "bus":
                                    transport = 3
                                elif trans_input == "underground":
                                    transport = 5
                                else:
                                    print("This type of transportation does not exist. Please enter taxi, bus, or underground.")
                                    continue
                                if multiple % transport != 0:
                                    print("This method of transportation is not possible.")
                                    continue
                            elif multiple > 1:
                                transport = multiple
                            else:
                                print("There is no connection to this node.")
                                continue
                            index = 0
                            if transport == 2:
                                index = 0
                            elif transport == 3:
                                index = 1
                            elif transport == 5:
                                index = 2
                            if d.resources[index] > 0 and player != misterx:
                                return 1
                            else:
                                print("You do not have enough resources for this mode of transportation.")
                                continue
                        elif map.node_list[target - 1].occupied == 2:
                            print("You found Mr. X!")
                            valid = True

                        else:
                            print("This node is occupied.")
                            continue
                    else:
                        print("This is not a valid point number.")
                        continue
            d.move(m.node_list[target-1], misterx, index)
            print("The", player.color, "player is now at", player.pos.number)
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
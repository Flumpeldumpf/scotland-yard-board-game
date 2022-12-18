import random
from map import map

class setup:
    def __init__(self):
        pass
    
    def start_of_game(self):
        print("-----SCOTLAND YARD-----")
        print("-----hunting mr. x-----")
        print("                       ")
        input("Press Enter To Continue...")

    def take_turn(self, player, map):
        d = player
        n = player.pos
        m = map
        player.print_resources()
        self.get_input_move(d,n,m)

    def get_input_move(self, player, node, map):
        d = player
        n = node
        m = map
        
        if (player.resources[0] == 0 and player.pos.bus == ['0']) or (player.resources[1] == 0 and player.pos.metro == ['0']):
            print("sorry bub! you can't move buddy. ha.")
            return
        else:
            valid = False
            while not valid:
                print("Input the point you would like to move to.")
                target = input()
                if (int(target) > 0 and int(target) < 200):
                    if map.node_list[int(target) - 1].occupied == 0:
                        multiple = n.check_connectivity(map.node_list[int(target)-1])
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
                        if d.resources[index] > 0:
                            valid = True
                        else:
                            print("You do not have enough resources for this mode of transportation.")
                            continue
                    else:
                        print("This node is occupied.")
                        continue
                else:
                    print("This is not a valid point number.")
                    continue
            d.move(m.node_list[int(target)-1], index)
            print("Player is now at", player.pos.number)

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
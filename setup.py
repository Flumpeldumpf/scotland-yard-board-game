import random
from map import map

class setup:
    def __init__(self):
        pass

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
        # are there any possible moves??????
        valid = False
        while not valid:
        print("Input the point you would like to move to.")
        target = input()
        # need to check to see if input is valid (and add loops for people to enter new input)
        multiple = n.check_connectivity(map.node_list[int(target)-1])
        print(multiple)
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
            if multiple % transport != 0:
                print("This method of transportation is not possible.")
        else:
            transport = multiple
        print(d.move(m.node_list[int(target)-1], transport))
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
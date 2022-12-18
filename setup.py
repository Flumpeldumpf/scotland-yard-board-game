import random

class setup:
    def __init__(self):
        pass
    
    def take_turn(self, detective, map):
        d = detective
        n = detective.pos
        m = map
        #print out resources and possible moves
        print("Input the point you would like to move to.")
        target = input()
        # need to check to see if input is valid (and add loops for people to enter new input)
        multiple = node.check_connectivity(map.node_list[int(target)-1], n)
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
                print("This type of transportation does not exist")
            if multiple % transport != 0:
                print("This method of transportation is not possible.")
        else:
            transport = multiple
        if transport == 2:
            transport = 0
        elif transport == 3:
            transport = 1
        elif transport == 5:
            transport = 2
        d.move(int(target), transport)
        
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
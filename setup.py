import random

class setup:
    def __init__(self):
        pass
    
    def take_turn(self, node):
        #print out resources and possible moves
        print("Input the point you would like to move to.")
        target = input()
        print("Input your method of transportation.")
        transport = input()
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
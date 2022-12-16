#configs
#How many players are there?
#
from map import map
from detective import detective

taxi = 2
bus = 3
metro = 5

def main():
    map1 = map([])
    map.makemap(map1)
    #map.return_map(map1)

    resources = [8, 6, 4]
    red = detective("red", map1.node_list[0], resources)
    yellow = detective("yellow", map1.node_list[1], resources)
    green = detective("green", map1.node_list[2], resources)
    blue = detective("blue", map1.node_list[3], resources)
    print(map1.node_list[9])
    print(red.move(map1.node_list[9], taxi))
    
#while (dectectives still have moves or mr.x is found)
#
#   facilitate mr. x's move(s)
#   
#   make the player's moves:
#       make player 1's move
#       make player 2's move etc.
#
if __name__ == "__main__":
    main()
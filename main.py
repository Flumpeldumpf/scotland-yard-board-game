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

    red = detective("red", map1.node_list[0], [10, 8, 4])
    map1.node_list[0].occupied = true;
    yellow = detective("yellow", map1.node_list[1], [10, 8, 4])
    green = detective("green", map1.node_list[2], [10, 8, 4])
    blue = detective("blue", map1.node_list[3], [10, 8, 4])

    print(red.move(map1.node_list[8], taxi))

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
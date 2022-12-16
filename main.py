#configs
#How many players are there?
#
from map import map

def main():
    map1 = map([])
    map.makemap(map1)
    map.return_map(map1)

    resources = [8, 6, 4]
    red = detective("red", 1, resources)
    yellow = detective("yellow", 2, resources)
    green = detective("green", 3, resources)
    blue = detective("blue", 4, resources)
    
#while (dectectives still have moves or mr.x is found)
#
#   facilitate mr. x's move(s)
#   
#   make the player's moves:
#       make player 1's move
#       make player 2's move etc.
#
#
#
#
if __name__ == "__main__":
    main()
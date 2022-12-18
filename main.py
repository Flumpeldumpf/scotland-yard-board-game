#configs
#How many players are there?
#
from map import map
from detective import detective
from setup import setup

taxi = 2
bus = 3
metro = 5

def main():
    map1 = map([])
    map.makemap(map1)
    #map.return_map(map1)

    st = setup()
    posList = st.generate_start_positions() 
    red = detective("red", map1.node_list[posList[0]], [10, 8, 4])
    map1.node_list[posList[0]].occupied = 1
    yellow = detective("yellow", map1.node_list[posList[1]], [10, 8, 4])
    map1.node_list[posList[1]].occupied = 1
    green = detective("green", map1.node_list[posList[2]], [10, 8, 4])
    map1.node_list[posList[2]].occupied = 1
    blue = detective("blue", map1.node_list[posList[3]], [10, 8, 4])
    map1.node_list[posList[3]].occupied = 1

    
    # print("red is at", red.pos.number, "where do you want to move?")
    # moveTo = int(input())
    # print(red.move(map1.node_list[moveTo-1], taxi))
    print(map1.find_shortest_route(map1.node_list[183], map1.node_list[67]))
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
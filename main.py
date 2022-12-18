# configs

from map import map
from player import player
from setup import setup

taxi = 2
bus = 3
metro = 5

def main():
    
    map1 = map([])
    map.makemap(map1)
    # map.return_map(map1)

    st = setup()
    st.start_of_game()
    posList = st.generate_start_positions() 
    player_list = []
    red = player("red", map1.node_list[posList[0]], [10, 8, 4, 0, 0])
    map1.node_list[posList[0]].occupied = 1
    player_list.append(red)
    yellow = player("yellow", map1.node_list[posList[1]], [10, 8, 4, 0, 0])
    map1.node_list[posList[1]].occupied = 1
    player_list.append(yellow)
    green = player("green", map1.node_list[posList[2]], [10, 8, 4, 0, 0])
    map1.node_list[posList[2]].occupied = 1
    player_list.append(green)
    blue = player("blue", map1.node_list[posList[3]], [10, 8, 4, 0, 0])
    map1.node_list[posList[3]].occupied = 1
    player_list.append(blue)
    misterx = player("black", map1.node_list[posList[4]], [4, 3, 3, 2, 4]) #TODO: change 4 to num of players
    map1.node_list[posList[4]].occupied = 1
    #player_list.append(misterx)
    
    turncount = 0
    while(turncount < 100):
        st.take_turn(player_list[turncount % 4],map1) #TODO: eventually turncount will need to be %
        turncount = turncount + 1
    # print("red is at", red.pos.number, "where do you want to move?")
    # moveTo = int(input())
    # print(red.move(map1.node_list[moveTo-1], taxi))
    print(map1.find_shortest_route(map1.node_list[183], map1.node_list[67]))
#
#
#   
#
if __name__ == "__main__":
    main()
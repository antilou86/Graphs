from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
connections = {}


#Traversal coooode 
def traversal(room, visited=None):
    exits = room.get_exits() # analyze exits
    if room.id in connections:# base case if all exits are explored
        if len(exits) == len(connections[room.id]): 
            if room.id in visited:
                return
    if visited == None:
        visited = set()
    visited.add(room.id) # add room to visited and connections
    if room.id not in connections:
        connections[room.id] = {}
    for e in exits: # set up loop to explore each unvisited exit
        if player.current_room.get_room_in_direction(e).id not in visited:
            #move to a side room
            if e not in connections[room.id]:
                player.travel(e)
                traversal_path.append(e)
                if len(player.current_room.get_exits()) == 1:#if there is only one exit, add it to visited.
                    visited.add(player.current_room.id)
            if player.current_room.id not in visited:
                traversal(player.current_room, visited)
            #move back to initial room
            way_back = ""
            if e == "n":
                way_back = "s"
            if e == "s":
                way_back = "n"
            if e == "w":
                way_back = "e"
            if e == "e":
                way_back = "w"
            if player.current_room.id not in connections:
                connections[player.current_room.id] = {}
            if way_back not in connections[player.current_room.id]:
                connections[player.current_room.id][way_back] = room.id
            player.travel(way_back)
            traversal_path.append(way_back)

# get initial room
player.current_room = world.starting_room
#traverse
traversal(player.current_room)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")

from room import Room
from random import choice, shuffle
from room_list import rooms
from item_list import starter_lantern, items

dungeon = [ [None for n in range(10)] for i in range(10)]
dungeon_data = [ [None for n in range(10)] for i in range(10)]

start_room = {
    'name': 'Outside Cave Entrance',
    'description': 'North of you, the cave mount beckons',
    'is_light': True,
    'exits': ('n',),
    'exits_for': ('s',),
    'has_treasure': False
}

def room_fits(c_room, pos_x, pos_y):
    """
    takes in a room and the desired x, y coordinates
    if x, y is empty and the room's exits match the exits
    of the surrounding room, returns True,
    else returns false
    """
    fits = True
    if dungeon_data[pos_x][pos_y] is not None:
        fits = False
    else:
        if pos_x - 1 == -1:
            if 'n' in rooms[c_room]['exits']:
                fits = False
        elif dungeon_data[pos_x - 1][pos_y] is not None:
            if 's' in dungeon_data[pos_x - 1][pos_y]['exits']:
                if 'n' not in rooms[c_room]['exits']:
                    fits = False
        if pos_y + 1 == 10:
            if 'e' in rooms[c_room]['exits']:
                fits = False
        elif dungeon_data[pos_x][pos_y + 1] is not None:
            if 'w' in dungeon_data[pos_x][pos_y + 1]:
                if 'e' not in rooms[c_room]['exits']:
                    fits = False
        if pos_x + 1 == 10:
            if 's' in rooms[c_room]['exits']:
                fits = False
        elif dungeon_data[pos_x + 1][pos_y] is not None:
            if 'n' in dungeon_data[pos_x + 1][pos_y]:
                if 's' not in rooms[c_room]['exits']:
                    fits = False
        if pos_y - 1 == -1:
            if 'w' in rooms[c_room]['exits']:
                fits = False
        elif dungeon_data[pos_x][pos_y - 1] is not None:
            if 'e' in dungeon_data[pos_x][pos_y - 1]:
                if 'w' not in rooms[c_room]['exits']:
                    fits = False
    return fits

def attach_rooms(room, x, y):
    """
    takes a room and cycles through directions, attaching rooms together
    if they connect
    """
    if x - 1 >= 0 and dungeon[x-1][y] is not None:
        n_room = dungeon_data[x-1][y]
        if 's' in n_room['exits']:
            room.n_to = dungeon[x-1][y]
            dungeon[x-1][y].s_to = room
    if y + 1 <= 9 and dungeon[x][y+1] is not None:
        e_room = dungeon_data[x][y+1]
        if 'w' in e_room['exits']:
            room.e_to = dungeon[x][y+1]
            dungeon[x][y+1].w_to = room
    if x + 1 <= 9 and dungeon[x+1][y] is not None:
        s_room = dungeon_data[x+1][y]
        if 'n' in s_room['exits']:
            room.s_to = dungeon[x+1][y]
            dungeon[x+1][y].n_to = room
    if y - 1 >= 0 and dungeon[x][y-1] is not None:
        w_room = dungeon_data[x][y-1]
        if 'e' in w_room['exits']:
            room.w_to = dungeon[x][y-1]
            dungeon[x][y-1].e_to = room

def construct_rooms(c_room, pos_x, pos_y):
    """
    takes the data for the last room created and it's position,
    then for each exit, filters for rooms with matching exit,
    then filters out those that won't connect to rooms around it
    from the remaining rooms it chooses one randomly, puts it in position
    then passes it to function to attach to surrounding rooms
    then calls construct room on the newly created room
    """
    for exit in c_room['exits']:
        fit_x = None
        fit_y = None
        if exit == 'n':
            fit_x = pos_x - 1
            fit_y = pos_y
        elif exit == 'e':
            fit_x = pos_x
            fit_y = pos_y + 1
        elif exit == 's':
            fit_x = pos_x + 1
            fit_y = pos_y
        elif exit == 'w':
            fit_x = pos_x
            fit_y = pos_y - 1
        a_rooms = [r for r in rooms if exit in rooms[r]['exits_for']]
        if len(a_rooms) > 0:
            a_rooms = [room for room in a_rooms if room_fits(room, fit_x, fit_y)]
            if len(a_rooms) > 0:
                chosen_room = rooms[choice(a_rooms)]
                dungeon_data[fit_x][fit_y] = chosen_room
                new_room = Room(chosen_room['name'], chosen_room['description'], chosen_room['is_light'])
                dungeon[fit_x][fit_y] = new_room
                attach_rooms(new_room, fit_x, fit_y)
                if chosen_room['has_treasure']:
                    shuffle(items)
                    dungeon[fit_x][fit_y].add_item(items.pop())
                construct_rooms(chosen_room, fit_x, fit_y)


def world_gen():
    """
    creates a room and inserts it at roughly center, south most position, and places
    data in the same spot in mirror array
    then passes the data to kick off construction
    when finished, returns the initial room that's connected to the others
    """
    dungeon[9][5] = Room(start_room['name'], start_room['description'], start_room['is_light'])
    dungeon[9][5].add_item(starter_lantern)
    dungeon_data[9][5] = start_room
    construct_rooms(start_room, 9, 5)
    return dungeon[9][5]

# Using another list of rooms, old list below
# rooms = {
#     'foyer': {
#         'name': 'Foyer',
#         'description': """Dim light filters in from the south. Dusty
#     passages run north and east.""",
#         'is_light': True,
#         'exits': ('s', 'e', 'n'),
#         'exits_for': ('n', 'w', 's')
#     },
#     'overlook': {
#         'name': 'Grand Overlook',
#         'description': """A steep cliff appears before you, falling
#     into the darkness. Ahead to the north, a light flickers in
#     the distance, but there is no way across the chasm.""",
#         'is_light': True,
#         'exits': ('s',),
#         'exits_for': ('n',)
#     },
#     'narrow': {
#         'name': 'Narrow Passage',
#         'description': """The narrow passage bends here from west
#     to north. The smell of gold permeates the air.""",
#         'is_light': True,
#         'exits': ('w', 'n'),
#         'exits_for': ('e', 's')
#     },
#     'treasure': {
#         'name': 'Treasure Chamber',
#         'description': """You've found the long-lost treasure
#     chamber! Sadly, it has already been completely emptied by
#     earlier adventurers. The only exit is to the south.""",
#         'is_light': True,
#         'exits': ('s',),
#         'exits_for': ('n',)
#     },
#     'n_cap': {
#         'name': 'Cap for North rooms',
#         'description': """Trying to see if directional capping helps""",
#         'is_light': True,
#         'exits': ('s',),
#         'exits_for': ('n',)
#     },
#     'e_cap': {
#         'name': 'Cap for East rooms',
#         'description': """Trying to see if directional capping helps""",
#         'is_light': True,
#         'exits': ('w',),
#         'exits_for': ('e',)
#     },
#     's_cap': {
#         'name': 'Cap for South rooms',
#         'description': """Trying to see if directional capping helps""",
#         'is_light': True,
#         'exits': ('n',),
#         'exits_for': ('s',)
#     },
#     'w_cap': {
#         'name': 'Cap for West rooms',
#         'description': """Trying to see if directional capping helps""",
#         'is_light': True,
#         'exits': ('e',),
#         'exits_for': ('w',)
#     },
# }
# These are for testing
# world_gen()
# for row in dungeon_data:
#     print(row)
# for row in dungeon:
#     print(row)

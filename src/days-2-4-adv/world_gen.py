from room import Room
from random import choice

min_room_count = 20
dungeon = [ [None for n in range(10)] for i in range(10)]
dungeon_data = [ [None for n in range(10)] for i in range(10)]

def world_gen():
    """
    creates a room and inserts it at roughly bottom, south most position, and places
    data in the same spot in mirror array
    then passes teh data to kick off construction
    when finished, returns the initial room that's connect to others
    """
    dungeon[9][5] = Room(start_room['name'], start_room['description'], start_room['is_light'])
    dungeon_data[9][5] = start_room
    construct_rooms(start_room, 9, 5)
    return dungeon[9][5]

def construct_rooms(c_room, pos_x, pos_y):
    """
    takes the data for the last room created and it's position,
    then for each exit filters for rooms with matching exit,
    then filters out those that won't connect to rooms around it
    """
    global min_room_count
    if min_room_count > 0:
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
                fit_y = pos_x - 1
            a_rooms = [r for r in rooms if exit in rooms[r]['exits_for']]
            if len(a_rooms) > 0:
                a_rooms = [room for room in a_rooms if room_fits(room, fit_x, fit_y)]
                if len(a_rooms) > 0:
                    chosen_room = rooms[choice(a_rooms)]
                    dungeon_data[fit_x][fit_y] = chosen_room
                    dungeon[fit_x][fit_y] = Room(chosen_room['name'], chosen_room['description'], chosen_room['is_light'])
                    attach_rooms(dungeon[fit_x][fit_y], fit_x, fit_y)
                    min_room_count -= 1
                    construct_rooms(chosen_room, fit_x, fit_y)

def room_fits(c_room, pos_x, pos_y):
    """
    takes in a room and x, y position and checks
    if it's exits match the rooms surrounding x, y
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
        if dungeon_data[pos_x][pos_y - 1] is not None:
            if 'e' in dungeon_data[pos_x][pos_y - 1]:
                if 'w' not in rooms[c_room]['exits']:
                    fits = False
    return fits

def attach_rooms(room, x, y):
    """
    takes a room and cycles through directions, attaching rooms together
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
            dungeon[x][y+1] = room.w_to
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

start_room = {
    'name': 'Outside Cave Entrance',
    'description': 'North of you, the cave mount beckons',
    'is_light': True,
    'exits': ('n',),
    'exits_for': ('s',)
}

rooms = {
    'foyer': {
        'name': 'Foyer',
        'description': """Dim light filters in from the south. Dusty
    passages run north and east.""",
        'is_light': True,
        'exits': ('s', 'e', 'n'),
        'exits_for': ('n', 'w', 's')
    },
    'overlook': {
        'name': 'Grand Overlook',
        'description': """A steep cliff appears before you, falling
    into the darkness. Ahead to the north, a light flickers in
    the distance, but there is no way across the chasm.""",
        'is_light': True,
        'exits': ('s',),
        'exits_for': ('n',)
    },
    'narrow': {
        'name': 'Narrow Passage',
        'description': """The narrow passage bends here from west
    to north. The smell of gold permeates the air.""",
        'is_light': True,
        'exits': ('w', 'n'),
        'exits_for': ('e', 's')
    },
    'treasure': {
        'name': 'Treasure Chamber',
        'description': """You've found the long-lost treasure
    chamber! Sadly, it has already been completely emptied by
    earlier adventurers. The only exit is to the south.""",
        'is_light': True,
        'exits': ('s',),
        'exits_for': ('n',)
    },
    'n_cap': {
        'name': 'Cap for North rooms',
        'description': """Trying to see if directional capping helps""",
        'is_light': True,
        'exits': ('s',),
        'exits_for': ('n',)
    },
    'e_cap': {
        'name': 'Cap for East rooms',
        'description': """Trying to see if directional capping helps""",
        'is_light': True,
        'exits': ('w',),
        'exits_for': ('e',)
    },
    's_cap': {
        'name': 'Cap for South rooms',
        'description': """Trying to see if directional capping helps""",
        'is_light': True,
        'exits': ('n',),
        'exits_for': ('s',)
    },
    'w_cap': {
        'name': 'Cap for West rooms',
        'description': """Trying to see if directional capping helps""",
        'is_light': True,
        'exits': ('e',),
        'exits_for': ('w',)
    },
}
# These are for testing
# world_gen()
# for row in dungeon_data:
#     print(row)
# for row in dungeon:
#     print(row)

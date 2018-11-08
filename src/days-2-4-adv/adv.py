from item import Item
from item import Treasure
from item import LightSource
from room import Room

#Declare all the items
item = {
    'rock': Item('rock', 'rock with the shape and size of an orange'),
    'log': Item('log', 'a small wooden log'), 
    'rope': Item('rope', '30 ft of rope'),
    'chair': Item('chair', 'generic chair'),
    'hat': Item('hat', 'a rain hat'),
    'hiking_pole': Item('hiking pole', 'a pole you use as a walking stick while hiking'),
    'treasure_chest': Item('treasure chest', 'a big treasure chest'),
    'shovel': Item('shovel', 'a big gardening shovel'),
    'treasure1': Treasure('treasure1', 'treasure1 description', 50),
    'treasure2': Treasure('treasure2', 'treasure2 description', 100),
    'treasure3': Treasure('treasure3', 'treasure3 description', 200),
    'lamp': LightSource('lamp', 'a small oil lamp')
}

# treasure = {
#     'treasure1': Treasure('treasure1', 'treasure1 description', 50),
#     'treasure2': Treasure('treasure2', 'treasure2 description', 100),
#     'treasure3': Treasure('treasure3', 'treasure3 description', 200)
# }


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item["rock"], item["log"], item["rope"]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item["lamp"], item["chair"]], False),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item['treasure1']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item["hat"], item["hiking_pole"]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item["treasure_chest"], item["shovel"]]),
}

# print(room['outside'].name)
# print(Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons", [item["rock"], item["log"], item["rope"]]).name)
# print(type(room))
# print(type(room['outside']))

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# print(room['outside'].n_to)
# print(item['rock'].description)



################ Main ################

# Make a new player object that is currently in the 'outside' room.
from player import Player
player1 = Player(input('\n'+'>>>Enter player name: '), room['outside'])

# Write a loop that:
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    # * If the user enters a cardinal direction, attempt to move to the room there.
    # * Print an error message if the movement isn't allowed.
    # * If the user enters "q", quit the game.
    # * Add functionality that prints out all the items that are visible to the player when they are in that room.
    # * Add a new type of sentence the parser can understand: two words in the form of [verb] [item] (e.g. take coins)

while True:
    lightCheck = player1.location.is_light or \
    True in [isinstance(player1.location.items[i], LightSource) for i in range(len(player1.location.items))] or \
    True in [isinstance(player1.items[i], LightSource) for i in range(len(player1.items))]

    if lightCheck:
        print('\n'+'Location Name: '+ player1.location.name + '\n'+ 'Location Description: '+ player1.location.description)
        print("Items in the room: ", [player1.location.items[i].name for i in range(len(player1.location.items))])
    else:
        print("It's pitch black!\n")    
        print("Items in the room: ", [player1.location.items[i].name for i in range(len(player1.location.items))])


    command = input('>>>Next move: ').split(' ')
    validDirections = ['n', 's', 'e', 'w']

    if command[0] in validDirections:
        dirAttr = command[0] + '_to'
        if hasattr(player1.location, dirAttr): #The arguments are an object and a string. The result is True if the string is the name of one of the object’s attributes, False if not.
            player1.location = getattr(player1.location, dirAttr)
        else:
            print('\n' +'Can\'t go that way! Please choose a different direction.')
    
    if command[0] == 'q':
        print('GAME OVER')
        break

    # if command[0] == ('get' or 'take'):
    #     if command[1] in [player1.location.items[i].name for i in range(len(player1.location.items))]:
    #         player1.location.removeItem(item[command[1]])
    #         player1.addItem(item[command[1]])
    #         if hasattr(item[command[1]], 'empty'): 
    #             if item[command[1]].empty == False:
    #                 player1.addScore(item[command[1]].value)
    #                 print(player1.score)
    #             else:
    #                 print(item[command[1]].name + ' is empty')
    #         item[command[1]].on_take()
    #     else: 
    #         print('Item not in room.')

    if command[0] == ('get' or 'take'):
        if lightCheck == False:
            print("Good luck finding that in the dark!")
        if command[1] in [player1.location.items[i].name for i in range(len(player1.location.items))]:
            player1.location.removeItem(item[command[1]])
            player1.addItem(item[command[1]])
            if hasattr(item[command[1]], 'value'): 
                if getattr(item[command[1]],'value') == 0:
                    print(item[command[1]].name+ ' is empty. Someone must have already taken the treasure inside.')
                else:
                    player1.addScore(item[command[1]].value)
                    print(player1.score)
            item[command[1]].on_take()
        else: 
            print('Item not in room.')
    
    if command[0] == 'drop':
        if command[1] in [player1.items[i].name for i in range(len(player1.items))]:
            player1.removeItem(item[command[1]])
            item[command[1]].on_drop()
            player1.location.addItem(item[command[1]])
        else:
            print('You don\'t have that item in your items.')
    
    if command[0] == ('i' or 'items'):
        print(command[0])
        print('Player items: ', player1.items)
    
    if command[0] == 'score':
        print('Player Score: ', player1.score)


    













# ##FIRST ATTEMPT 
# # Make a new player object that is currently in the 'outside' room.
# from player import Player
# player1 = Player('Bob', 'treasure')

# # Write a loop that:
# #
# # * Prints the current room name
# # * Prints the current description (the textwrap module might be useful here).
# # * Waits for user input and decides what to do.

# for key in player_1.__dict__:
#     if key == 'location': 
#         for key in room:
#             if key == player_1.location:
#                 print(room[player_1.location].name)
#                 print(room[player_1.location].description)
#         nextMove = input("Enter next move: ")

        
# # If the user enters a cardinal direction, attempt to move to the room there.
# # Print an error message if the movement isn't allowed.
# #
# # If the user enters "q", quit the game.


# # if nextMove == 'n':
# #     if player_1.location == room[player_1.location].n_to.name:
# #     # player_1.location = room['foyer']
# #         print(player_1.location)
# #     else:
# #         print(player_1.location)

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

# if nextMove == 'n':
#     if player_1.location == 'outside' or player_1.location == 'foyer' or player_1.location == 'narrow':
#         player_1.location = room[player_1.location].n_to.name
#         print(player_1.location)
#     else:
#         print('Movement not allowed!')
#         # nextMove = input("Enter next move: ")


# if nextMove == 's':
#     if player_1.location == 'foyer' or player_1.location == 'overlook' or player_1.location == 'treasure':
#         player_1.location = room[player_1.location].s_to.name
#         print(player_1.location)
#     else:
#         print('Movement not allowed!')
#         # nextMove = input("Enter next move: ")

# if nextMove == 'e':
#     if player_1.location == 'foyer':
#         player_1.location = room[player_1.location].s_to.name
#         print(player_1.location)
#     else:
#         print('Movement not allowed!')
#         # nextMove = input("Enter next move: ")

# if nextMove == 'w':
#     if player_1.location == 'narrow':
#         player_1.location = room[player_1.location].s_to.name
#         print(player_1.location)
#     else:
#         print('Movement not allowed!')
#         # nextMove = input("Enter next move: ")

# if nextMove == 'g': 
#     print('GAME OVER')
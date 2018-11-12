from room import Room
from player import Player
from item import Item

# Declare all the rooms
item = {
    'rock':  Item("rock",
                     "heavy, solid"),

    'log':    Item("log", "fireable stuff"),

    'match': Item("match", "to light"),

    'hat':   Item("hat", "protect yourself from the spiders"),

    'gold': Item("gold", "collect them"),
}
print(item['rock'].name)
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['rock'], item['hat']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item['log']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item['match']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item['hat']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item['gold'], item['hat']]),
}



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
# Make a new player object that is currently in the 'outside' room.
# print(room['outside'].n_to)

player= Player(input("\n Enter player name: "), room['outside'])

# Write a loop that:
def start_game():


# * Prints the current room name
    print('Welcome {}, you are in {}, {}'.format(player.name, player.location.name, player.location.description))
    print("This room has the following items: ", [player.location.items[i].name for i in range(len(player.location.items))])
    while True: 
        valid_dir = ['n', 's', 'w', 'e']
        inputs1 = input('\n Enter a command:').split(" ")
        if inputs1[0] =="q":
            print("Thanks for playing! Bye!")
            break

        if inputs1[0] in valid_dir:
            x = inputs1[0] + '_to'
            if hasattr (player.location, x):
                player.location = getattr(player.location, x)
                print(player.location.name, player.location.description)
                print("This room has the following items: ", [player.location.items[i].name for i in range(len(player.location.items))])
            else:
                print("Player can't go this direction")
        if inputs1[0] == 'take':
            if inputs1[1] in [player.location.items[i].name for i in range(len(player.location.items))]:
                player.take(item[inputs1[1]])
                # print("You picked: ")
                print("Your backpack has the following items: ", [player.items[i].name for i in range(len(player.items))])
                player.location.drop(item[inputs1[1]])
                print("This room has the following items: ", [player.location.items[i].name for i in range(len(player.location.items))])
        if inputs1[0] == 'drop':
            if inputs1[1] in [player.items[i].name for i in range(len(player.items))]:
                player.drop(item[inputs1[1]])
                # print("You picked: ")
                print("Your backpack has the following items: ", [player.items[i].name for i in range(len(player.items))])
                player.location.take(item[inputs1[1]])
                print("This room has the following items: ", [player.location.items[i].name for i in range(len(player.location.items))])
            else:
                print("This room doesn't have this item")
        else:
            print('Please, enter valid command')
        
   

start_game()
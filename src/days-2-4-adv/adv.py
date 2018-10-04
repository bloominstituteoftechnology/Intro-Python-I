from player import Player
from room import Room
from item import Item, Treasure


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by 
earlier adventurers. The only exit is to the south."""),
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


knife = Item("knife", "Old rusty knife that looks like it hasn't been sharpened in a decade")
lamp = Item("lamp", "It's always good to have a source of light")
leather_pouch = Item("leather_pouch", "Look inside... There might be something in there!")
wine_flask = Item("wine_flask", "Well it's empty so what's the point?")
golden_key = Item("golden_key", "You never know when you will come across a locked door")
rope = Item("rope", "It's about 10 feet long and made out of horse hair")
ancient_scroll = Item("ancient_scroll", "Looks like a love letter, does it hold any value?")

pearls = Treasure("pearls", "So shiny, so white, so pretty. Maybe this has some value?", 100)
emerald = Treasure("emerald", "Looks dirty, but it still has a glimmer to it", 200)
gold_coins = Treasure("gold_coins", "These got to be worth a lot!", 500)



room['outside'].items = [knife, lamp, pearls]
room['foyer'].items = [leather_pouch, wine_flask, gold_coins]
room['overlook'].items = []
room['narrow'].items = [golden_key, rope]
room['treasure'].items = [ancient_scroll, emerald]

#
# Main
#
print()
print("\nWelcome! Are you ready to embark on an adventure?")
print("=========================================================")
name = input(" What is your name?   ")
room = room['outside']
player = Player(name, room)
print()
print(f'Welcome, {player.name}!\n Lets begin the journey!')
print()
print("To play this game, use the buttons n, e, w, and s for direction. \n\n n = North \n e = East \n w = West \n s = South \n q = Quit")
print("=========================================================")
print()
print("There are items in each room that can be collected.")
print("You can only take one item from room at a time ")
print("To take item ---- use command 'get [item you choose]'-----")
print("To drop an item ---- use the command 'drop [item you choose]'------- ")
print("You can drop an item anywhere, but can only pick up an item if it is present in the room")
print("You can check your inventory at any point in time by using command 'inventory'")
print("=========================================================")
print()
print("You can look around your surrounding without leaving a room.")
print("To do that, just add look before a direction")
print("=========================================================")
print()
print("The ultimate goal of this game is get to the treasure before anyone else gets to it.")
print("Be careful to not fall to your death!")
print()
print("=========================================================")
print("LET'S BEGIN!")
print("=========================================================")

# Write a loop that:

while True:
    print()
    print(f'Current Room: {player.room.name}...')
    print(player.room.description)
    print()
    print("=========================================================")
    print('Items in room include:')
    for items in player.room.items:
        print(f'{items.name}: {items.description}')
    print("=========================================================")

    cmds = input("What's Next? -->  ").split(' ')

    error = "You cannot go this way!! Try again"
    valid_directions = ["n", "e", "w", "s"]
    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        elif cmds[0] == "inventory":
            print('Inventory:')
            for items in player.items:
                print(f'{items.name}: {items.description}')
        elif cmds[0] == "score":
            print(f'Score: {player.score}')
        elif cmds[0] in valid_directions:
            player.travel(cmds[0])
        else:
            print("The command entered does not exist.")
            print()
    if cmds[0] == "look":
        if cmds[1] in valid_directions:
            player.look(cmds[1])
    if cmds[0] == "get":
        if cmds[1]:
            player.getItem(cmds[1])
        else:
            print('Please specify which item to get from inventory')
    if cmds[0] == "drop":
        if cmds[1]: 
            player.removeItem(cmds[1])
        else:
            print('Please specify which item to remove from inventory')
    

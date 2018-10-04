from player import Player
from room import Room
from item import Item, Treasure, Goblet

#ITEM DICTIONARY
item = {
    'treasure_chest': Item("TREASURE_CHEST", "The chest is bejeweled and beautiful beyond your wildest dreams."),

    'peasant_sword': Item("PEASANT_SWORD", "It is a dull sword with damage of 1."),

    'pile_of_discarded_food': Item("PILE_OF_DISCARDED_FOOD", "You see it is a pile of delicious rubbish that will grant you 5+ health."),

    'goblet': Goblet(),
}  

#ROOM DICTIONARY
room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons."),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


#ROOM LINKS
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#ROOM ITEMS
room['outside'].addItems(item['treasure_chest'])
room['outside'].addItems(item['peasant_sword'])
room['outside'].addItems(item['pile_of_discarded_food'])

room['foyer'].addItems(item['goblet'])

#PLAYER CONSOLE
player = Player(input("What is your name? "), room['outside'])

while True:
    player.currentRoom.examine()
    cmd = input("\nWhat's your next move, pal? (Actions: n, s, e, w, status, get [item], drop [item], i/inventory)\n").lower().split(" ")
    
    if len(cmd) == 1:
        if cmd[0] == 'q':
            break
        elif cmd[0] == 'n':
            print('\n== You stride confidently north. ==')
            try: 
                player.playerMove('n')
            except: 
                print(player.badMove)
        elif cmd[0] == 's':
            print('\n== You stride confidently south. ==')
            try: 
                player.playerMove('s')
            except: 
                print(player.badMove)
        elif cmd[0] == 'e':
            print('\n== You stride confidently east. ==')
            try: 
                player.playerMove('e')
            except: 
                print(player.badMove)
        elif cmd[0] == 'w':
            print('\n== You stride confidently west. ==')
            try: 
                player.playerMove('w')
            except: 
                print(player.badMove)
        elif cmd[0] == 'i' or cmd[0] == 'inventory':
            print(f'\n== You have the following items in your sack: {player.items} ==')
        elif cmd[0] == 'status':
            print(f'\n{player}')            
        else:
            print("\n== You wander aimlessly like a fool and will surely be eaten by goblins if you don't pick a direction soon. ==")
    else:
        if cmd[0] == 'get':
            if len(player.currentRoom.items) == 0:
                 print(f"\n== There are no items in the room. You gawk vacantly into the distance like one who has seen far too many dragons in their days. ==")
            elif len(player.currentRoom.items) > 0:
                player.playerGet(cmd[1])
                player.currentRoom.items.remove(item[cmd[1]])
            else:
                print(f"\n== There are no items in the room called '{cmd[1]}'. You gawk vacantly into the distance like one who has seen far too many dragons in their days. ==")
        elif cmd[0] == 'drop':
            if cmd[1] in player.items:
                player.playerDrop(cmd[1])
                player.currentRoom.addItems(item[cmd[1]])
            else:
                print(f"\n== There are no items in your sack called '{cmd[1]}''. You gawk vacantly into the distance like one who has seen far too many dragons in their days. ==")            
        else:
            print("\n== Nothing you are saying makes sense. Insanity is looming just beyond another fawlty keystroke. ==")


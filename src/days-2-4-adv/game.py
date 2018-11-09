from item import Item
from player import Player
from room import Room

room = {
    'outside': Room(
        "Outside Cave Entrance", "North of you, the cave mount beckons"),

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

room['outside'].items = ['sword', 'wand', 'shield']

# items = {
#     'sword': Item('sword').get_item(),
#     'wand': Item('wand').get_item(),
#     'treasure': Item('treasure').get_item()
# }
#
# p1 = Player('Brian', 'outside', [])
# p1.items.append(items['sword'])
#
# print(p1)


def play_game():

    player_name = input("Player name >> ").strip()
    player = Player(player_name, 'outside')
    invalid_option = "Invalid direction"

    def player_items_string():
        if len(player.items) < 1:
            return "No Items In Inventory"
        elif len(player.items) == 1:
            return str(player.items[0]).capitalize()
        else:
            return ", ".join(player.items).capitalize()

    def room_items_string():
        if len(room[player.room].items) < 1:
            return "No Items In Room"
        elif len(room[player.room].items) == 1:
            return str(room[player.room].items).capitalize()
        else:
            return ", ".join(room[player.room].items).capitalize()

    while True:
        # Print Room Info along with Player info
        print("\n")
        print("Current Room Name: " + room[player.room].name)
        print("Room Description: " + room[player.room].description)
        print("Room Items: " + room_items_string())
        print("Player Name: " + player.name)
        print("Player Items: " + player_items_string())
        print("\n")

        choice = input("Choose a direction to travel, press q to quit, i for inventory, weapon name to pick up,"
                       " [drop item_name] to drop item in different room >> ").strip().lower()
        print("\n")
        print("Choice: " + str(choice.split()))

        # Quit Game
        if choice == 'q':
            break

        # Drop item in whatever room you are in
        if choice.split()[0] == 'drop' and choice.split()[1] in player.items:
            player.items.remove(choice.split()[1])
            room[player.room].items.append(choice.split()[1])
        elif choice.split()[0] == 'drop' and choice.split()[1] not in player.items:
            print("Item Not In Inventory")

        # Add item to inventory from current room
        if choice in room[player.room].items:
            room[player.room].items.remove(choice)
            player.items.append(choice)
        elif choice not in room[player.room].items and choice.split()[0] != "drop":
            print("Item Not In Room")

        if choice in ['n', 's', 'e', 'w', 'north', 'south', 'east', 'west']:
            # Outside to Foyer
            if player.room == 'outside' and choice[0][0] == 'n':
                player.room = 'foyer'
            elif player.room == 'outside' and choice[0][0] != 'n':
                print(invalid_option)
            # Foyer to Outside
            elif player.room == 'foyer' and choice[0][0] == 's':
                player.room = 'outside'
            # Foyer to Overlook
            elif player.room == 'foyer' and choice[0][0] == 'n':
                player.room = 'overlook'
            # Foyer to Narrow
            elif player.room == 'foyer' and choice[0][0] == 'e':
                player.room = 'narrow'
            elif player.room == 'foyer' and choice[0][0] == 'w':
                print(invalid_option)
            # Overlook to Foyer
            elif player.room == 'overlook' and choice[0][0] == 's':
                player.room = 'foyer'
            elif player.room == 'overlook' and choice[0][0] in ['n', 'e', 'w', 'north', 'east', 'west']:
                print(invalid_option)
            # Narrow to Foyer
            elif player.room == 'narrow' and choice[0][0] == 'w':
                player.room = 'foyer'
            # Narrow to Treasure
            elif player.room == 'narrow' and choice[0][0] == 'n':
                player.room = 'treasure'
            elif player.room == 'narrow' and choice[0][0] in ['n', 'w', 'north', 'west']:
                print(invalid_option)
            # Treasure to Narrow
            elif player.room == 'treasure' and choice[0][0] == 's':
                player.room = 'narrow'

play_game()

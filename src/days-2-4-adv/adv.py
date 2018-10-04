import textwrap
from room import Room
from player import Player
from weapon import Weapon
# Declare all the rooms

room = {
    'b1': Room(
        "b1",
        "Blue Basement",
        """This is Blue Basement. Another typical spawn point for the blue team.
            There is pretty good cover and a BR (Battle-Rifle) respawns here."""),

    'b2':  Room(
        'b2',
        "Blue Objective",
        """This is where Blue team spawns. Another popular name for 
    this location is Blue Objective as it is where the flag would 
    appear in CTF & where you plant the bomb on Assault"""),

    'b-needles': Room('b-needles',
                      "Blue Needles", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'b-eli': Room('b-eli', "Blue Eli", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'b-door':    Room('b-door', "Front Door of Blue", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'b-street': Room('b-street', "Blue Pink Street", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'b-nerd': Room('b-nerd', "Blue Pink 3 Nerd Ledge", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'p1':   Room('p1', "Under Pink Tower", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'p2': Room('p2', "Inside Pink Tower", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'p2-door': Room('p2-door', "Pink Tower's Front Door", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'p3': Room('p3', "On top of Pink Tower", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'r-nerd': Room('r-nerd', "Red Pink 3 Nerd Ledge", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'r-street': Room('r-street', "Red Pink Street", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'r-needles': Room('r-needles', "Red Needles", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'r-eli': Room('r-eli', "Red Eli", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'r-door':    Room('r-door', "Front Door of Red", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'r1': Room('r1', "Red Basement", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'r2': Room('r2', "Red Objective", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'mid1': Room('mid1', "Bottom Middle", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'mid2': Room('mid2', "Top Middle", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'sword': Room('sword', "Sword Platform", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'car1': Room('car1', "Bottom Carbine", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'car2': Room('car2', "Inside Carbine", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'car3': Room('car3', "Top Carbine", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'b-toilet': Room('b-toilet', "Blue Toilet", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'b-car': Room('b-car', "Carbine side of Blue Base", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'b-bubble': Room('b-bubble', "Blue Carbine Bubble", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'b-slide': Room('b-slide', "Blue Carbine Ramp", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'r-toilet': Room('r-toilet', "Red Toilet", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'r-car': Room('r-car', "Carbine side of Red Base", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'r-bubble': Room('r-bubble', "Red Carbine Bubble", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

weapon = {
    "Sword" : Weapon("\nSword", "The energy sword is a one slice kill. It can only be used on enemies that get too close\n"),
    "Frag Grenade" : Weapon("\nFrag Grenade", "A short fused grenade that if timed correctly can bring a bang to the battlefield!\n"),
    "Plasma Grenade": Weapon("\nPlasma Grenade", "Blue glowing grenades from the Covenant. Also called stickies, They have a longer fuse and can stick to enemies\n"),
    "Needler" : Weapon("\nNeedler", "A gun that shoots prickly needles. It is not very powerful if your opponent is moving but if they stand still like Ronald then they are done son!\n"),
    "Shotgun" : Weapon("\nShotgun", "The UNSC's trusty close quarters weapon. Although you have to be really really close for it to be effective\n"),
    "Battle Rifle" : Weapon("\nBattle Rifle", "The standard weapon of any hardcore Halo kid. Your utility weapon that can be effective at all ranges but shines in medium -> close range battles. 4 consecutive shots for a kill\n"),
    "Carbine" : Weapon("\nCarbine", "The Covenants medium range rifle. It shoots faster than a Battle Rifle but you also need to land more shots to kill\n"), 
}

# print (weapon["Sword"])
# print(room["b1"])
# print(room['r-bubble'])
# Link rooms together
# All paths from blue perspective!
# Blue 2 Paths
room['b2'].w_to = room['b-door']
room['b2'].a_to = room['b-needles']
room['b2'].s_to = room['b1']
room['b2'].d_to = room['b-car']
# Blue 1 Paths
room['r1'].w_to = room['b-door']
room['r1'].a_to = room['b-eli']
room['r1'].s_to = room['b2']
# Blue Needles Paths
room['b-needles'].w_to = room['b-street']
room['b-needles'].s_to = room['b2']
room['b-needles'].d_to = room['b-eli']
# Blue Eli Paths
room['b-eli'].w_to = room['p1']
room['b-eli'].a_to = room['b-needles']
room['b-eli'].s_to = room['b1']
# Blue Street Paths
room['b-street'].w_to = room['p2']
room['b-street'].s_to = room['b-needles']
room['b-street'].a_to = room['b-nerd']
room['b-street'].d_to = room['p1']
# Pink 2 Paths
room['p2'].w_to = room['r-street']
room['p2'].s_to = room['b-street']
room['p2'].d_to = room['p2-door']
# Red Street Paths
room['r-street'].w_to = room['r-needles']
room['r-street'].s_to = room['p2']
room['r-street'].a_to = room['r-nerd']
room['r-street'].d_to = room['p1']
# Red Needles Paths
room['r-needles'].w_to = room['r2']
room['r-needles'].s_to = room['r-street']
room['r-needles'].d_to = room['r-eli']
# Red 2 Paths
room['r2'].w_to = room['r1']
room['r2'].a_to = room['r-needles']
room['r2'].s_to = room['r-door']
room['r2'].d_to = room['r-car']
# Red 1 Paths
room['r1'].w_to = room['r2']
room['r1'].a_to = room['r-eli']
room['r1'].s_to = room['r-door']
# Red Eli Paths
room['r-eli'].w_to = room['r1']
room['r-eli'].a_to = room['r-needles']
room['r-eli'].s_to = room['p1']
# Pink 1 Paths
room['p1'].w_to = room['r-eli']
room['p1'].s_to = room['b-eli']
room['p1'].d_to = room['mid1']
# Blue Carbine Side Paths
room['b-car'].w_to = room['car2']
room['b-car'].a_to = room['b2']
room['b-car'].d_to = room['b-toilet']
# Carbine 2 Paths
room['car2'].w_to = room['r-car']
room['car2'].s_to = room['b-car']
room['car2'].a_to = room['car1']
# Carbine 1 Paths
room['car1'].w_to = room['r-door']
room['car1'].s_to = room['b-door']
room['car1'].a_to = room['mid1']
# Bottom Middle Paths
room['mid1'].w_to = room['r-door']
room['mid1'].s_to = room['b-door']
room['mid1'].a_to = room['p1']
room['mid1'].d_to = room['car1']
# Weapon Assignments
room['car2'].weaponsIn.append(weapon["Carbine"])
# Slide/ Car 3/ P3 / Bubble & Car 1 Paths not added/complete yet due to height/drop/pathing limitations currently


#
# Main
#
valid_directions = {"w": "w", "a": "a", "s": "s", "d": "d",
                    "forward": "w", "left": "a", "backwards": "s", "right": "d"}
# Make a new player object that is currently in the 'outside' room.
player = Player(input("What is your name? "), room["b2"])

currentRoomDesc = room[player.currentRoom.label].description

while True:
    commands = input("-> ").lower().split(" ")
    if len(commands) == 1:
        if commands[0] == "q":
            break
        elif commands[0] in valid_directions:
            player.movement(valid_directions[commands[0]])
        elif commands[0] == "look":
            player.look()
        else:
            print("Please enter a valid command.")
    else:
        if commands[0] == "look":
            if commands[1] in valid_directions:
                player.look(valid_directions[commands[1]])
            
            else:
                print("Please enter a valid command.")
        
    # print(player.currentRoom)
    # print(currentRoomDesc)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

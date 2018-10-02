from room import Room

# Declare all the rooms

room = {
    'b1':    Room("Blue Basement", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'b2':  Room("Blue Objective",
                "North of you, the cave mount beckons"),

    'b-needles': Room("Blue Needles", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'b-eli': Room("Blue Eli", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'b-door':    Room("Front Door of Blue", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'b-street': Room("Blue Pink Street", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'b-nerd': Room("Blue Pink 3 Nerd Ledge", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'p1':   Room("Under Pink Tower", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'p2': Room("Inside Pink Tower", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'p2-door': Room("Pink Tower's Front Door", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'p3': Room("On top of Pink Tower", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'r-nerd': Room("Red Pink 3 Nerd Ledge", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'r-street': Room("Red Pink Street", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'r-needles': Room("Red Needles", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'r-eli': Room("Red Eli", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'r-door':    Room("Front Door of Red", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'r1': Room("Red Basement", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'r2': Room("Red Objective", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'mid1': Room("Bottom Middle", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'mid2': Room("Top Middle", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'sword': Room("Sword Platform", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'car1': Room("Bottom Carbine", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'car2': Room("Inside Carbine", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'car3': Room("Top Carbine", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'b-toilet': Room("Blue Toilet", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'b-car': Room("Carbine side of Blue Base", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'b-bubble': Room("Blue Carbine Bubble", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'b-slide': Room("Blue Carbine Ramp", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'r-toilet': Room("Red Toilet", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'r-car': Room("Carbine side of Red Base", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'r-bubble': Room("Red Carbine Bubble", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

print(room["r-bubble"])
# Link rooms together
# All paths from blue perspective!
# Blue 2 Paths
room['b2'].w_to = room['b-door']
room['b2'].a_to = room['b-needles']
room['b2'].s_to = room['b1']
room['b2'].d_to = room['b-car']
#Blue 1 Paths
room['r1'].w_to = room['b-door']
room['r1'].a_to = room['b-eli']
room['r1'].s_to = room['b2']
#Blue Needles Paths
room['b-needles'].w_to = room['p-slide']
room['b-needles'].s_to = room['b2']
room['b-needles'].d_to = room['b-eli']
#Blue Eli Paths
room['b-eli'].w_to = room['p1']
room['b-eli'].a_to = room['b-needles']
room['b-eli'].s_to = room['b1']
#Blue Street Paths
room['b-street'].w_to = room['p2']
room['b-street'].s_to = room['b-needles']
room['b-street'].a_to = room['b-nerd']
room['b-street'].d_to = room['p1']
#Pink 2 Paths
room['p2'].w_to = room['r-street']
room['p2'].s_to = room['b-street']
room['p2'].d_to = room['p2-door']
#Red Street Paths
room['r-street'].w_to = room['r-needles']
room['r-street'].s_to = room['p2']
room['r-street'].a_to = room['r-nerd']
room['r-street'].d_to = room['p1']
#Red Needles Paths
room['r-needles'].w_to = room['r2']
room['r-needles'].s_to = room['r-street']
room['r-needles'].d_to = room['r-eli']
#Red 2 Paths
room['r2'].w_to = room['r1']
room['r2'].a_to = room['r-needles']
room['r2'].s_to = room['r-door']
room['r2'].d_to = room['r-car']
#Red 1 Paths
room['r1'].w_to = room['r2']
room['r1'].a_to = room['r-eli']
room['r1'].s_to = room['r-door']
#Red Eli Paths
room['r-eli'].w_to = room['r1']
room['r-eli'].a_to = room['r-needles']
room['r-eli'].s_to = room['p1']
#Pink 1 Paths 
room['p1'].w_to = room['r-eli']
room['p1'].s_to = room['b-eli']
room['p1'].d_to = room['mid1']
#Blue Carbine Side Paths
room['b-car'].w_to = room['car2']
room['b-car'].a_to = room['b2']
room['b-car'].d_to = room['b-toilet']
#Carbine 2 Paths
room['car2'].w_to = room['r-car']
room['car2'].s_to = room['b-car']
room['car2'].a_to = room['car1']
#Carbine 1 Paths
room['car1'].w_to = room['r-door']
room['car1'].s_to = room['b-door']
room['car1'].a_to = room['mid1']
#Bottom Middle Paths
room['mid1'].w_to = room['r-door']
room['mid1'].s_to = room['b-door']
room['mid1'].a_to = room['p1']
room['mid1'].d_to = room['car1']

#Slide/ Car 3/ P3 / Bubble & Car 1 Paths not added/complete yet due to height/drop/pathing limitations currently






#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

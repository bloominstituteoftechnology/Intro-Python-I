# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.

from sys import exit 
from random import randint 
from threading import Timer 
import os 

class Scene(object): 

    def enter(self): 
        exit(1)

class Engine(object): 

    def __init__(self, room): 
        self.room = room #self = game room = cave 

    def play(self): 
        current_room = self.room.opening_room() # roomOne() 
        last_room = self.room.next_room('final')

        while current_room != last_room: 
            next_room_name = current_room.enter() #roomOne() begins #roomTwo() begins
            current_room = self.room.next_room(next_room_name) 

        current_room.enter() 

        os._exit(0)

class RoomOne(Room): 
    def enter(self): 
        print('''
        You are outside the cave entrance. As you can see the cave mouth beckons.
        
        You must type "north" to enter the cave.
        ''')
        
        action = input("> ")
        
        while True: 
            if action === 'north': 
                break
            else: 
                print('Invalid input.')
                action = input('> ')
                continue

        return 'room_two'

class RoomTwo(Room): 
    def enter(self): 
        print('''
            You are in the foyer of the cave. The dim light filters in from the south.
            Dusty passages run the north and east.' 

            Type "north" to overlook, "south" to go back outside, or "east" to go east.
            '''
        )
        
        action = input('> ')

        while True: 
            if action == 'north' or action == 'south' or action == 'east': 
                break 
            else 
                print('Invalid input')
                action = input('> ')
                continue
        
        if action == 'north': 
            return 'room_three'
        else if action == 'south': 
            return 'room_one'
        else 
            return 'room_four'

class RoomThree(Room): 
    def enter(self): 
        print(''' 
            A steep cliff appears before you, falling into the darkness. 
            Ahead to the north, a light flickers in the distance, but there 
            is no way accross the chasm.''

            Type "south" to go south.
            '''
        )

        action = input('> ') 

        while True: 
            if action == 'south': 
                break
            else: 
                print('Invalid input')
                action = input('> ')
                continue 
        
        return 'room_two'

class RoomFour(self): 
    def enter(self): 
        print('''
            The narrow passage bends here from the west to the north. The smell of gold permeates the air.", 

            Type "west" to go west or type "north" to go north.
            '''
        )

        action = input('> ')

        while True: 
            if action == 'west': 
                break
            else if action == 'north': 
                break
            else: 
                print('Invalid input')
                action = input('> ')
                continue 

        if action ='west': 
            return 'room_two'
        else: 
            return 'room_five'




   "treasure": {
        "name": "Treasure Chamber",
        "description": """You've found the long-lost treasure
chamber. Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        "s_to": "narrow",
    },

}
    
class Map(object): 

    rooms = {
        'room_one': RoomOne(), 
        'room_two': RoomTwo(), 
        'room_three': RoomThree(), 
        'room_four': RoomFour(), 
        'room_five': RoomFive(),
        'final': Final()
    }

    def __init__(self, start_room): 
        self.start_room = start_room # room_one

    def next_room(self, room_name): 
        val = Map.rooms.get(room_name) 
        return val 

    def opening_room(self): # game
        return self.next_room(self.start_room)

def Trapped(): 
    print('\nYou are trapped in the cave and you will die.')
    os._exit(0)

t = Timer(300, Trapped) 
t.start() 
cave = Map('room_one') 
game = Engine(cave) 
game.play() 

rooms = {


    

    

 

""" template room to copy into code
    "room": {
        "name": "",
        "description": "",
        "n_to": "",
        "s_to": "",
        "e_to": "",
        "w_to": "",
    },
"""

# Write a class to hold player information, e.g. what room they are in currently

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

print('''
    You are a world renowned treasure hunter who is in a mission to find    the greatest treasure on earth. There is an urban legend that procla    ims that the Cave of Souls is rumored to contain the greatest treasu    re on earth.''') 



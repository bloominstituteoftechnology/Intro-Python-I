# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.
# These are the existing rooms. Add more as you see fit.
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

from sys import exit
from textwrap import dedent
from threading import Timer 
import os 

class Room(object): 

    def enter(self): 
        exit(1)

class RepeatTimer(object): 
    
    def __init__(self, interval, function): 
        self.interval = interval
        self.function = function 
    
    def start(self):
        self.timer = Timer(self.interval, self.function)
        self.timer.start() 
    
    def cancel(self):
        self.timer.cancel() 

class Engine(RepeatTimer): 

    def Trapped(self): 
        print('\nYour time has run out and you are now trapped in the cave forever!')
        os._exit(0)
    
    def __init__(self, room): 
        self.room = room 
        super().__init__(300, self.Trapped)

    def play(self): 
        current_room = self.room.opening_room()  
        beginning_room = self.room.next_room('room_one')
        second_room = self.room.next_room('room_two')

        while current_room: 
            next_room_name = current_room.enter()
            current_room = self.room.next_room(next_room_name) 

            if current_room == beginning_room: 
                self.cancel()
            elif current_room == second_room: 
                self.start()

class RoomOne(Room): 
    def enter(self): 
        print(dedent('''
            You are about to arrive at the cave entrance. As you can see the cave mouth beckons, 
            but also as you approach the cave you notice a homeless man laying by the entrace. 
            He tells you "Any one who enters the Cave of Souls has only 5 minutes to leave or 
            they will be trapped inside the cave forever.'
        
            Type "north" to enter the cave or "quit" to quit the game.
        '''))

        action = input("> ")
        
        while True: 
            if action == 'north': 
                break
            elif action == 'quit': 
                os._exit(0)
            else: 
                print('Invalid input.')
                action = input('> ')
                continue

        return 'room_two'

class RoomTwo(Room): 
    def enter(self): 
        print(dedent('''
            You are now located at the central foyer of the cave. The dim light filters in 
            from the south side. Dusty passages run through the north and east sides.' 

            Type "north" to overlook, "south" to go back outside, "east" to go east or "quit" to quit the game.
            '''
        ))
        
        action = input('> ')

        while True: 
            if action == 'north' or action == 'south' or action == 'east': 
                break 
            elif action == 'quit': 
                os._exit(0)
            else: 
                print('Invalid input')
                action = input('> ')
                continue
        
        if action == 'north': 
            return 'room_three'
        elif action == 'south': 
            return 'room_one'
        else: 
            return 'room_four'

class RoomThree(Room): 
    def enter(self): 
        print(dedent(''' 
            A steep cliff appears before you, falling into the darkness. 
            Ahead to the north side, a light flickers in the distance, but there 
            is no way accross the chasm.''

            Type "south" to go south or "quit" to quit the game.
            '''
        ))

        action = input('> ') 

        while True: 
            if action == 'south': 
                break
            elif action == 'quit': 
                os._exit(0)
            else: 
                print('Invalid input')
                action = input('> ')
                continue 
        
        return 'room_two'

class RoomFour(Room): 
    def enter(self): 
        print(dedent('''
            The narrow passage bends here from the west to the north. The smell of gold permeates the air.", 

            Type "west" to go west, type "north" to go north or "quit" to quit the game.
            '''
        ))

        action = input('> ')

        while True: 
            if action == 'west': 
                break
            elif action == 'north': 
                break
            elif action == 'quit': 
                os._exit(0)
            else: 
                print('Invalid input')
                action = input('> ')
                continue 

        if action == 'west': 
            return 'room_two'
        else: 
            return 'room_five'

class RoomFive(Room): 
    def enter(self): 
        print(dedent(''' 
            You have found the long-lost treasure chamber. Sadly, 
            it has already been completely emptied by earlier 
            adventurers. The only exit is to go south.

            Type "south" to go south or "q" to quit the game.
        '''
        ))

        action = input('> ')

        while True: 
            if action == 'south': 
                break 
            elif action == 'quit': 
                os._exit()
            else: 
                print('Invalid input')
                action = input('> ')
                continue
        
        return 'room_four'

class Map(object): 

    rooms = {
        'room_one': RoomOne(), 
        'room_two': RoomTwo(), 
        'room_three': RoomThree(), 
        'room_four': RoomFour(), 
        'room_five': RoomFive()
    }

    def __init__(self, start_room): 
        self.start_room = start_room

    def next_room(self, room_name): 
        val = Map.rooms.get(room_name) 
        return val 

    def opening_room(self): 
        return self.next_room(self.start_room)

print(dedent('''
    You are a world renowned treasure hunter who is in a mission to find the 
    greatest treasure on earth. There is an urban legend that proclaims that 
    the Cave of Souls is rumored to contain the greatest treasure on earth. 
    
    Do you want to enter the Cave of Souls? 

    Type "yes" to enter the cave or "no" to quit the game.
''')) 

action = input('> ')

while True: 
    if action == 'yes': 
        cave = Map('room_one') 
        game = Engine(cave) 
        game.play() 
    elif action == 'no': 
        os._exit(0)
    else: 
        print('Invalid input')
        action = input('> ')
        continue



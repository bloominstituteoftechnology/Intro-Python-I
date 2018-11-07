import random
import sys
import os

print("\nPractice\n")

name = "Lucas"
print(name)

# + - * / % ** //

print("5 / 2 =", 5/2)
print("5 * 2 =", 5*2)
print("5 % 2 =", 5%2)
print("5 ** 2 =", 5**2)

quote = "\"Always remember you are unique"

multi_line_quote = '''just like 
everyone else '''

print("\n\n%s %s %s\n" % ('I like the quote', quote, multi_line_quote))

#
# WALKTHROUGH with TEACH
#

from room import Room


class Player:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        self.health = 100
        self.inventory = []
        self.movement_speed = 10

    def pickup_item(self, item):
        self.inventory.append(item)

    def try_move(self, direction):
        # Try to move in a direction, print 'error' if unable to go that way
        d = direction + "_to"
        # Check to see if move is possible
        if not hasattr(self.currentRoom, d):
            print("You can't go that way!")
            return self.currentRoom
        else:
            self.currentRoom = self.currentRoom[d]

room = Room("Outside", "outside")
foyer = Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.")
room.n_to = foyer
foyer.s_to = room

p = Player(room)
print(p.currentRoom)
p.currentRoom = room.n_to
print(p.currentRoom)

p.try_move('s')
print(p.currentRoom)


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"Name: {self.name}, description: {self.description}"

r = Room("Outside", "outside")
f = Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.")

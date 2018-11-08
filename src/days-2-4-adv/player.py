from room import Room
from item import Item
#__________________LECTURE NOTES_________________________________
# 'self' = 'this' (more or less)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# "__init__" is a reserved method in python classes. It is known as a constructor in 
# object oriented concepts. This method is called when an object is created from the class 
# and it allows the class to initialize the attributes of said class.
#_____________________________________________________________________________

# Write a class to hold player information, e.g. what room they are in
# currently.
#________________________________________________________________________

#item Dictionary, why 'here'? b/c we are Calling items (making specific items from the 
# Item Classs blueprint) to Player here. Items belongs to Player. Making new Ninjas lol
#obj name = {
#   'new key name': Class Name blueprint we are drawing from("name", "descrption, these are the properties from the Class")},
#    'next key': .......
items = {
    'pickle': Item("Pickle", '''Can be thrown, or be a delicious snack'''),
    'skull': Item("Skull", '''A morbid reminder of your own mortality'''),
    'boot': Item("Boot", '''A singular old boot, I wonder where the other one is...'''),
    'trash': Item("Trash", '''This is trash...'''),
    'puppy': Item("Puppy", '''It's a puppy! Oh what a good boy!'''),
    'toothpick': Item("Toothpick", '''Might come in handy later?'''),
    'butterfly': Item("Butterfly", '''Maybe we can let this go outside?'''),
}

class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.inventory = []
    
    def lookAround(self, direction = None):
        if direction is None:
            print(f'{self.name} you step into the {self.currentRoom}')
        else:
            nextRoom = self.currentRoom.roomDirection(direction)
            if nextRoom is not None:
                print(f'{self.name} you see the {nextRoom}')
            else:
                print(f'{self.name} sorry this room is empty.')


    def travel(self, direction):
        nextRoom = self.currentRoom.roomDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
        else:
            print("Your path is blocked, try a different way.")
    
    def grabItem(self, item):
        if len(self.currentRoom.inventory) > 0 and item in self.currentRoom.inventory:
            self.inventory.append(item)
            self.currentRoom.removeItem(item)
            print(f'You grabbed the {item}')
        else:
            print('no items found sorry...')
            
    def dropItem(self, item):
        if len(self.inventory) > 0 and item in self.inventory:
            self.inventory.remove(item)
            self.currentRoom.addItem(item)
            print(f'{item} dropped...litter bug.')
        else:
            print('No such item found in bag...maybe you dropped it?')
    
    def lookInventory(self):
        if len(self.inventory) > 0:
            print("What's in your wallet?")
            for item in self.inventory:
                print(f'{items[item].name}: {items[item].description}')
        else:
            print("nothing but lint in here, sorry buddy.")

#________Lecture Example________________________
# class Player:
#     def __init__(self, currentRoom):
#         self.currentRoom = currentRoom
#         self.health = 100
#         self.inventory = []
        
#     def.pickup_item(self, item):
#         self.inventory.append(item)

#     def try_move(self, direction):
#         """
#         Picka direction, or print error stating player can not go that way
#         """
#         #making attribute expectations for adv.py directions
#         d = direction + "_to"
#         #check to see if movement is possible  in direction chosen
#         # python check called HASATTR: hasattr(object, name)
#         # The arguments are an object and a string. The result is True if the string is the name of
#         # one of the object’s attributes, False if not. (This is implemented by calling getattr(object, name) 
#         # and seeing whether it raises an exception or not.)
#         if not hasattr(self.currentRoom, d):
#             print("The path is blocked, choose a different door...")
#             return self.currentRoom
#         else:
#             self.currentRoom = self.currentRoom[d]
            #



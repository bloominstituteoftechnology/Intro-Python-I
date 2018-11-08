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

# item Dictionary, why 'here'? b/c we are Calling items (making specific items from the 
# Item Classs blueprint) to Player here. Items belongs to Player. Making new Ninjas lol
# obj name = {
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
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    def look_around(self, direction = None):
        if direction is None:
            print(f'{self.name} you step into the {self.current_room}')
        else:
            next_room = self.current_room.room_direction(direction)
            if next_room is not None:
                print(f'{self.name} you see the {next_room}')
            else:
                print(f'{self.name} sorry this room is empty.')


    def travel(self, direction):
        next_room = self.current_room.room_direction(direction)
        if next_room is not None:
            self.current_room = next_room
        else:
            print("Your path is blocked, try a different way.")
    
    def grab_item(self, item):
        if len(self.current_room.inventory) > 0 and item in self.current_room.inventory:
            self.inventory.append(item)
            self.current_room.remove_item(item)
            print(f'You grabbed the {item}')
        else:
            print('no items found sorry...')
            
    def drop_item(self, item):
        if len(self.inventory) > 0 and item in self.inventory:
            self.inventory.remove(item)
            self.current_room.add_item(item)
            print(f'{item} dropped...litter bug.')
        else:
            print('No such item found in bag...maybe you dropped it?')
    
    def look_inventory(self):
        if len(self.inventory) > 0:
            print("\nWhat's in your wallet?")
            for item in self.inventory:
                print(f"---{items[item].name}: {items[item].description}---")
                print(f"\n{self.name}, what lovely items you've collected... \nShall we continue on our journey?")
                print(f'\n{self.current_room}')
        else:
            print("nothing but lint in here, sorry buddy.")

#________Lecture Example________________________
# class Player:
#     def __init__(self, current_room):
#         self.current_room = current_room
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
#         if not hasattr(self.current_room, d):
#             print("The path is blocked, choose a different door...")
#             return self.current_room
#         else:
#             self.current_room = self.current_room[d]
            



from room import Room
#__________________LECTURE NOTES_________________________________
# 'self' = 'this' (more or less)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# "__init__" is a reserved method in python classes. It is known as a constructor in 
# object oriented concepts. This method is called when an object is created from the class 
# and it allows the class to initialize the attributes of said class.
#_____________________________________________________________________________

# Write a class to hold player information, e.g. what room they are in
# currently.

# class Player():
#     def __init__(self, name, current_room):
#         self.name = name
#         self.current_room = current_room
#     def __str__(self):
#         return str(f'{self.name} you are in {self.current_room}')

class Player:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        self.health = 100
        self.inventory = []
        
    def.pickup_item(self, item):
        self.inventory.append(item)

    def try_move(self, direction):
        """
        Picka direction, or print error stating player can not go that way
        """
        #making attribute expectations for adv.py directions
        d = direction + "_to"
        #check to see if movement is possible  in direction chosen
        # python check called HASATTR: hasattr(object, name)
        # The arguments are an object and a string. The result is True if the string is the name of
        # one of the object’s attributes, False if not. (This is implemented by calling getattr(object, name) 
        # and seeing whether it raises an exception or not.)
        if not hasattr(self.currentRoom, d):
            print("The path is blocked, choose a different door...")
            return self.currentRoom
        else:
            self.currentRoom = self.currentRoom[d]
            #



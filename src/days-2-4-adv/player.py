# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom):
        # starting attributes of the class
        self.name = name # player name
        self.currentRoom = currentRoom # player current room
    def travel(self, direction): # player travel function
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        # nextRoom = invoking a function from room.py
        # that moves player in the inputed direction from the players current room
        if nextRoom is not None: # if player moves in any direction
            self.currentRoom = nextRoom # nextRoom becomes player currentRoom
            print(nextRoom) # display current room
        else:
            print("You cannot move in that direction.") # displays message is player connot move in intended direction
    def look(self, direction=None):
        if direction is None: # if player is not looking in a particular direction
            print(self.currentRoom) # name of current room displays
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction) 
            # nextRoom = invoking a function from room.py
            # that moves player in the inputed direction from the players current room
            if nextRoom is not None: # if player sees another room in any direction
                print(nextRoom) # display name of that room
            else:
                print("There is nothing there.") # if no room is avaiable in that direction, print message
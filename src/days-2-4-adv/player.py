# Write a class to hold player information, e.g. what room they are in
# currently.


class Player(object):
    def __init__(self, name, currentRoom, items = []):
        self.name = name
        self.currentRoom = currentRoom
        self.items = items
        self.points = 0 

    def __str__(self):
        return f"{self.name} \n\ncurrently in room {self.currentRoom}\n"
    
    def room_change(self, direction):
        newRoom = self.currentRoom.change_room(direction)
        print(f"newRoom === {newRoom}") #sole purpose of this line is for debugging
        if newRoom is not None:
            self.currentRoom = newRoom
            return "Changing rooms..."
        else:
            return "You cannot go into that direction!"
    
    #

        

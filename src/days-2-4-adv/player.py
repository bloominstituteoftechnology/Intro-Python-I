from items import Items

class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room
        Items.__init__(self, ['knife'])
    def changeRoom(self, direction):
        next_room = self.room.getRoomInDirection(direction)
        if next_room == None:
            print("There is nothing there.")
        else: 
            self.room = next_room
            print(self.room)
    def playerItems(self):
        Items.getItems(self, self.name)
        # print(f"\n you currently have {self.items}")
    def addObject(self, newObject):
        self.object = newObject
    def dropObject(self):
        self.object = 'nothing'
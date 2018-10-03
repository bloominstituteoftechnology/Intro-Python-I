from items import Items

class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room
        Items.__init__(self, self.name, ['knife'])
    def changeRoom(self, direction):
        next_room = self.room.getRoomInDirection(direction)
        if next_room == None:
            print(f"\nLocation unchanged. There is nothing {direction}.")
        else: 
            self.room = next_room
            print(f'\nYou are currently: \n{self.room}')
    def lookRoom(self, direction):
        next_room = self.room.getRoomInDirection(direction)
        if next_room == None:
            print(f"\nThere is nothing {direction}.")
        else: 
            print(f'\nGoing {direction} will take you to: \n{next_room}')
    def playerItems(self):
        Items.getItems(self, self.name)
    def addItem(self, newItem):
        Items.addItem(self, newItem)
        # Items.getItems(self, self.name)
    def dropItem(self, newItem):
        Items.dropItem(self, newItem)
        # Items.getItems(self, self.name)
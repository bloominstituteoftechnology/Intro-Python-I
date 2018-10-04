# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, items = [], score = 0 ):
        self.name = name
        self.room = room
        self.items = items
        self.score = score
    def travel(self, direction):
        new_room = self.room.get_rooms(direction)
        if new_room:
            self.room = new_room
    def look(self, direction):
        new_room = self.room.get_rooms(direction)
        if new_room:
            print(f'LOOKING into the {new_room.name}')
        else:
            print('Your nose in a brick wall man! Chose another direction to look at before you embarass yourself!')
    def getItem(self, item):
        # if the item is in the room, then append the item to the items in Player's class
        chosen = ''
        for items in self.room.items:
            if items.name == item:
                chosen = items
        self.items.append(chosen)
        self.room.remove_item(chosen)
        print('Current Inventory:')
        for items in self.items:
            print(f'{items.name}: {items.description}')
        # remove the item from the room
    def removeItem(self, item):
        chosen = ''
        for items in self.items:
            if items.name == item:
                chosen = items
        self.items.remove(chosen)
        self.room.add_item(chosen)
        print('Current Inventory:')
        for items in self.items:
            print(f'{items.name}: {items.description}')
    
    

        
        

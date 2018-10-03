# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room, inventory):
        self.name = name
        self.room = room
        self.inventory = inventory
        
    def grab_item(self, item):
        self.inventory.append(item)

    def check_inventory(self):
        print('You have the following items: ')
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(item.name + '--' + item:description)
        else:
            print('You have no items.')

    def getRoom(self):
        print('You are in the' + self.room.name + '.  ' + self.room.description)

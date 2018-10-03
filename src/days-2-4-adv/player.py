# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room, inventory):
        self.name = name
        self.room = room
        self.inventory = inventory

    def get_item(self, item):
        self.inventory.append(item)
    
    def drop_item(self, index):
        if len(self.inventory) is 0:
            print('Oops, your inventory is totally empty!')
        else:
            del self.inventory[index]

    def check_inventory(self):
        
        if len(self.inventory) is not 0:
            print('Your inventory contains: ')
            for i, item in enumerate(self.inventory):
                print(str(i) + ' --> ' + item)
        else:
            print('You are broke. Nothing in the bag!!!')
        
    def getRoom(self):
        print(75 * '#')
        print('You are in: ' + self.room.name)
        print('Directions: ' + self.room.description)
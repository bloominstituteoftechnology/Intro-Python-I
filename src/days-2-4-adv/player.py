# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    
    def __init__(self, name, room, inventory, score):
        self.name = name
        self.room = room
        self.inventory = inventory
        self.score = score

    def get_item(self, item):
        self.inventory.append(item)
        if isinstance(item.value, int):
            self.score += item.value
        else:
            self.score += 100
    
    def drop_item(self, index):
        if len(self.inventory) is 0:
            print('\nOops, nothing to drop, your inventory is totally empty!')
        else:
            del self.inventory[index]

    def check_inventory(self):
        if len(self.inventory) is not 0:
            print('\nYour inventory contains: ')
            for i, item in enumerate(self.inventory):
                print(str(i) + ' --> ' + item.name + ': ' + item.description)
        else:
            print('\nYou are broke. Nothing in the bag!!!')
        
    def getRoom(self):
        print(75 * '#')
        print('You are in: ' + self.room.name)
        print('                 ' + self.room.description)

    def getScore(self):
        print('Your score is: ' + str(self.score))
# Write a class to hold player information, e.g. what room they are in
# currently.

# Add capability to add Items to the player's inventory. 
# The inventory can also be a list of items "in" the player, similar to how Items can be in a Room.

class Player:
    def __init__(self, playerName, startLocation, inventory = None, score = None):
        self.name = playerName
        self.location = startLocation
        if inventory is None:
            inventory = []
        self.inventory = inventory
        if score is None:
            score = 0
        self.score = score

    def __repr__(self):
        # return f'Player({self.name!r}, {self.location!r}'
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.location!r}, {self.inventory!r})')
    
    def addItems(self, items):
        self.inventory.extend(items)
    
    def removeItem(self, item):
        self.inventory.remove(item)


    
# p1 = Player('Adrian', 'Living Room')

# print(p1)
# print(p1.name)
# print(p1.location)
# print(p1.inventory)


# p1.addItems(['sword', 'gun', 'grenades'])
# print(p1)
# print(p1.inventory)





##ASIDE
# for key in p1.__dict__:
#     if key == 'location':
#         print(p1.location)





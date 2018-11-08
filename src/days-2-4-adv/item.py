# This will be the base class for specialized item types to be declared later.

class Item:
    def __init__(self, itemName, itemDescription):
        self.name = itemName
        self.description = itemDescription

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.description!r})')
    
    def on_take(self):
        print('on_take for item class: ', self.name, 'was just picked up')

class Treasure(Item):
    def __init__(self, name, description, value):
        Item.__init__(self, name, description)
        self.value = value
        self.empty = False
    
    def on_take(self):
        self.empty = True
        print('on_take for treasure class: ', self.name, 'was just picked up')


# i = Treasure('b', 'a', 500)
# i.on_take()
# if i.empty:
#     print(True)

# item1 = Item('rock', 'huge boulder')
# print(item1)
# print(item1.name)
# print(item1.description)

# treasure1 = Treasure('gold bricks', 'shiny polished gold bricks', '$150000')
# print(treasure1.value)
# print(treasure1.name)
# print(treasure1.description)
# print(repr(treasure1))
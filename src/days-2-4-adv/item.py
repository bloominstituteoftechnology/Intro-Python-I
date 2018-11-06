# This will be the base class for specialized item types to be declared later.

class Item:
    def __init__(self, itemName, itemDescription):
        self.name = itemName
        self.description = itemDescription

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.description!r})')


class Treasure(Item):
    def __init__(self, name, description, value):
        Item.__init__(self, name, description)
        self.value = value



# item1 = Item('rock', 'huge boulder')
# print(item1)
# print(item1.name)
# print(item1.description)

# treasure1 = Treasure('gold bricks', 'shiny polished gold bricks', '$150000')
# print(treasure1.value)
# print(treasure1.name)
# print(treasure1.description)
# print(repr(treasure1))
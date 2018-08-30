# This will be the base class for specialized item types to be declared later.

class Item:
    def __init__(self, itemName, itemDescription):
        self.name = itemName
        self.description = itemDescription

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.name!r}, {self.description!r})')
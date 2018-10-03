# Add an Item class in a file item.py.
# This will be the base class for specialized item types to be declared later.
#The item should have name and description attributes.
#Hint: the name should be one word for ease in parsing later.

# base class
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description  
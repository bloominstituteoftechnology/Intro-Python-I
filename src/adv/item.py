# Add an `Item` class in a file `item.py`.

# This will be the _base class_ for specialized item types to be declared
# later.

# The item should have `name` and `description` attributes.

# Hint: the name should be one word for ease in parsing later.

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

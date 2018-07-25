# Implement a class to hold room information. This should have name and
# description attributes.

# Add capability to add items to rooms.

# The `Room` class should be extended with a `list` that holds the `Item`
# that are currently in that room.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.Items = []

    def addItem(self, item):
        self.Items.append(item)
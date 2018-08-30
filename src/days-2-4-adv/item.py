class Item():
    """The base class for all items"""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return "{}, {}".format(self.name, self.description)

class Item:
    def __init__(self, name, description):
        self.name = name # name should only be one word for ease in parsing later.
        self.description = description

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return "Current used item: {}".format(self.item_name)

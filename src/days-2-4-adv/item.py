
class Item:
    def __init__(self, item_name, description):
        self.item_name = item_name
        self.description = description

    def __repr__(self):
        return "Current used item: {}".format(self.item_name)

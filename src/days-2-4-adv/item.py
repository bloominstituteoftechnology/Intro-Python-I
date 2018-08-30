
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return "Current used item: {}".format(self.item)

    def addItem(self, item):
        self.items.append(item)

    def item_description(self):
        return self.description

    def item_drop(self):
        print(f"\nYou messed up and dropped {self.name} and cannot move forward!!!")

class Inventory:
    def __init__(self):
         self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

class Item:
    def __init__(self, item_name="", item_description=""):
        self.item_name = item_name
        self.item_description = item_description

    def print_desc(self):
        return "Item: {}, {}".format(self.item_name, self.item_description)
    
    def __repr__(self):
        return "{}".format(self.item_name)

    def __str__(self):
        return "{}".format(self.item_name)
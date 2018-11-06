# this will be the super class for all items
# the closest I could find to virtual functions is to have them raise a NotImplementedError
class Item:
    def __init__(self, name):
        self.name = name

    # on_take method to be treated as a virtual function to be overriden by child classes
    def on_take(self):
        raise NotImplementedError

    # on_drop method to be treated as a virtual function to be overriden by child classes
    def on_drop(self):
        raise NotImplementedError

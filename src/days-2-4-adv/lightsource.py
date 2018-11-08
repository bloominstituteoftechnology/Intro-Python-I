from item import Item

class LightSource(Item):
    def __init__(self, name):
        Item.__init__(self, name)

    def on_take(self): pass

    def on_drop(self):
      print("\nEnable night vision. no wait we don't have night vision! Lets not drop that light!")
#Item class

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Treasure(Item):
    def __init__(self, name, description, value):
        Item.__init__(self, name, description)
        self.value = value
        self.picked_up = False
    def onTake(self):
        self.picked_up = True

# class LightSource(Item):
#     def __init__(self, name, description, calories):
#         Item.__init__(self, name, description)
#         self.calories = calories
#     def eat(self):
#         return self.calories
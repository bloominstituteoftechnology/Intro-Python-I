class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return f'{self.name}'
    def __str__(self):
        return f'{self.name}'
    def getDescription(self):
        return self.description
    def on_drop(self):
        print(f'\nYou have dropped {self.name}')

# class Food(Item):
#     def __init__(self, name, description, calories):
#         Item.__init__(self, name, description)
#         self.calories = calories
#     def getDescription(self):
#         return self.description + f'\nIt seems to have {self.calories.'
#     def eat(self):
#         return

class Treasure(Item):
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    def on_take()
    
class LightSource(Item):
    def __init__(self)

    def on_drop(self):
        print "It's not wise to drop your source of light!"
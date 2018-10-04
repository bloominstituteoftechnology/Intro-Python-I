class Item (object):
    
    def __init__(self, name, description): 
        self.name = name 
        self.description = description
        self.light = False
    def __repr__(self):
        return f"The item name is {self.name}. Description : {self.description}."
    def on_take(self):
        return "This item maybe useful.."
    def on_drop(self):
        return "No use for this item right now but remember where you dropped it. Might come in handy later.."

class Treasure(Item):
    def __init__(self,value, name, description):
        self.value = value
        super(Treasure,self).__init__(name, description)
    def on_take(self):
        return "Points collected maybe time to dump this sucker."
    def on_drop(self):
        return "Well you have already collected the points."

class LightSource(Item):
    def __init__(self, name, description):
        self.light = True
        return super(LightSource, self).__init__(name, description)
    def on_take(self):
        return "Keep your light with you at all times."
    def on_drop(self):
        return "It's not wise to drop your source of light!"
        
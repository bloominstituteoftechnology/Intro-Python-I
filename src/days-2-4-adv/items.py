class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.score_counter = 1
    def __repr__(self):
        return f"{self.name} - {self.description}"
    def __str__(self):
        return f"{self.name}"
    def getDescription(self):
        return self.description\

class Treasure(Item):
    def __init__(self, name, description, value):
        Item.__init__(self,name, description)
        self.value = value
        self.score_counter = 1
    def getDescription(self):
        return self.description + f"\n You could sell this for {self.value} gil! "
    def on_take(self):
        if self.score_counter > 0:
            self.score_counter -= 1
        return self.value
    def on_drop(self):
        return self.value

class LightSource(Item):
    def __init__(self, name, description):
        Item.__init__(self, name, description)
    def on_drop(self):
        print("Don't drop this, goofy.")

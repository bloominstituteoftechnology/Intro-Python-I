
class Item:
    def __init__(self,name,descr):
        self.name = name
        self.descr = descr
    
class Treasure(Item):
    def __init__(self,name,descr,value,picked_up):
        super().__init__(name,descr)
        self.value = value
        self.picked_up = picked_up
    

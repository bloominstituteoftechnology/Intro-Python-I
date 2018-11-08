# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room, inventory): 
        self.name = name
        self.room = room
        self.inventory = inventory

    
    def __repr__(self):
        for item in self.inventory:
            print(str(item.item_name)) 
            print(str(item.description))
            return
            
            


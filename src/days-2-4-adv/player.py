# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,name,current_location):
        self.name=name
        self.current_location=current_location
        self.possessions=[]
    def travel(self,direction):
        next_room=self.current_location.get_next_room(direction)
        if next_room==None:
            return f'Error: Player {self.name} is unable to move in {direction} direction.'
        else:    
            self.current_location=next_room
            return f'Moving {direction} you arrive at: {self.current_location.name}\n{self.current_location}'      
    def pickup(self,item):
        if item in self.current_location.inventory:
            self.current_location.inventory.remove(item)
            self.possessions.append(item)
            return f'{self.name} Picked up a {item}'
        else:
            return f'Cannot find {cmd[1]} in {self.current_location.name}'
    def i(self):
        item_arr=', '.join(self.possessions)
        return f'Items currently in possession: {item_arr}'
    def inventory(self):
        item_arr=', '.join(self.possessions)
        return f'Items currently in possession: {item_arr}'
    def drop(self,item):
        if item in self.possessions:
            self.possessions.remove(item)
            self.current_location.inventory.append(item)
            return f'{self.name} Dropped a {item}'
        else:
            return f'You do not have a {item} to drop.'
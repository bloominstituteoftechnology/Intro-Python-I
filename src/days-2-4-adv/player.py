# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,name,current_location):
        self.name=name
        self.current_location=current_location
        self.possessions=[]
        self.score=0
    def travel(self,direction):
        next_room=self.current_location.get_next_room(direction)
        if next_room==None:
            return f'Error: Player {self.name} is unable to move in {direction} direction.'
        else:    
            self.current_location=next_room
            return f'Moving {direction} you arrive at: {self.current_location.name}\n{self.current_location}'      
    def pickup(self,item):
        for element in self.current_location.inventory:
            if element.name[0]==item:
                self.current_location.inventory.remove(element)
                self.possessions.append(element)
                value=element.on_take()
                if value is not None:
                    self.score+=value
                return f'{self.name} picked up a {item}'
        return f'Cannot find {item} in {self.current_location.name}'
    def inventory(self):
        item_arr=[]
        for item in self.possessions:
            item_arr.extend(item.name)
        item_arr=', '.join(item_arr)
        return f'Items currently in possession: {item_arr}'
    def drop(self,item):
        for element in self.possessions:
            if element.name[0]==item:
                self.possessions.remove(element)
                self.current_location.inventory.append(element)
                warning=element.on_drop()
                if warning is not None:
                    print(f'{warning}')
                return f'{self.name} dropped a {item}'
        return f'You do not have a {item} to drop.'
    def get_score(self):
        return f'{self.name}\'s score:{self.score}'
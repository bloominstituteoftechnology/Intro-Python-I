# Write a class to hold player information, e.g. what room they are in
# currently.
from item import LightSource
class Player:
    def __init__(self,name,current_location):
        self.name=name
        self.current_location=current_location
        self.possessions=[]
        self.score=0
        self.can_see=False
    def travel(self,direction):
        next_room=self.current_location.get_next_room(direction)
        if next_room==None:
            return f'Error: Player {self.name} is unable to move in {direction} direction.'
        else:    
            self.current_location=next_room
            lighted=self.is_there_light()
            if lighted==None:
                return f'Moving {direction} you arrive at: {self.current_location.name}\n{self.current_location}'   
            else:
                return f'Moving {direction} you arrive at: {self.current_location.name}\n{self.current_location}\n{lighted}'   
    def pickup(self,item):
        if self.can_see==False:
            return 'Good luck finding that in the dark!'
        else:
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
    def is_there_light(self):
        if self.current_location.is_light==True:
            self.can_see=True
            return "The room is bright."
        else:
            for item in self.current_location.inventory:
                if isinstance(item,LightSource):
                    self.can_see=True
                    return "There's a light source illuminating the room."
            for item in self.possessions:
                if isinstance(item,LightSource):
                    self.can_see=True
                    return "Your light source illuminates the room." 
        self.can_see=False
        return "It's pitch black!"
        
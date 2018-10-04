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
            element=self.current_location.find_item(item)
            if element==None:
                return f'Cannot find {item} in {self.current_location.name}'
            else:
                self.current_location.remove_item(element)
                self.add_item(element)
                value=element.on_take()
                if value is not None:
                    self.score+=value
                return f'{self.name} picked up a {item}'
    def find_item(self,item):
        for element in self.possessions:
            if element.name[0]==item:
                return element
        return None
    def add_item(self,item):
        self.possessions.append(item)
    def remove_item(self,item):
        self.possessions.remove(item)
    def inventory(self):
        if len(self.possessions)==0:
            return 'You have no items in your possession'
        else:
            return f"Items currently in possession: {', '.join([item.name[0] for item in self.possessions])}"
    def drop(self,item):
        element=self.find_item(item)
        if element is not None:
            self.remove_item(element)
            self.current_location.add_item(element)
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
    def win(self):
        if self.score==2700:
            print('You have won the game.')
        return None
        
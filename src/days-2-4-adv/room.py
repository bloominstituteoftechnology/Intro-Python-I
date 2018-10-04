# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self,name,description,is_light):
        self.name=name
        self.description=description
        self.inventory=[]
        self.is_light=is_light
        self.n_to=None
        self.s_to=None
        self.e_to=None
        self.w_to=None
    def __str__(self):
        if len(self.inventory)==0:
            return f'name: {self.name}\ndescription: {self.description}\nThere is nothing of value here.'
        else:
            return f"name: {self.name}\ndescription: {self.description}\nitems available: {', '.join([item.name[0] for item in self.inventory])}"
    def get_next_room(self,direction):
        next_location=''
        if direction=='n':
            if hasattr(self,'n_to'):
                next_location=self.n_to
        elif direction=='e':
            if hasattr(self,'e_to'):
                next_location=self.e_to
        elif direction=='s':
            if hasattr(self,'s_to'):
                next_location=self.s_to
        elif direction=='w':
            if hasattr(self,'w_to'):
                next_location=self.w_to
        return next_location
    def find_item(self,item):
        for element in self.inventory:
            if element.name[0]==item:
                return element
        return None
    def add_item(self,item):
        self.inventory.append(item)
    def remove_item(self,item):
        self.inventory.remove(item)

# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self,name,description,illuminated):
        self.name=name
        self.description=description
        self.inventory=[]
        self.illuminated=illuminated
        self.n_to=None
        self.s_to=None
        self.e_to=None
        self.w_to=None
    def __str__(self):
        item_arr=[]
        for item in self.inventory:
            item_arr.extend(item.name)
        item_arr=', '.join(item_arr)
        return f'Current Location:\nname: {self.name}\ndescription: {self.description}\nitems available: {item_arr}'
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

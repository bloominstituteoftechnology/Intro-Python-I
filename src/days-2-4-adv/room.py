# Implement a class to hold room information. This should have name and
# description attributes. 

class Room (object):
    
    def __init__(self, name, description,items = [], n_to = None, s_to = None, e_to = None, w_to = None):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.directions = [] 
        # if len(self.name) > 0 : 
        #     self.__get_directions()
    # def __get_directions (self):
    #     print("getting Directions")
    #     directions = []
    #     if self.n_to is not None:
    #         directions.append("n")
    #     if self.s_to is not None:
    #         directions.append("s")
    #     if self.e_to is not None:
    #         directions.append("e")
    #     if self.w_to is not None:
    #         directions.append("w")
    #     self.directions = directions

    def __str__(self):
        return f"Room Name: {self.name}\n\n, Room description: {self.description}\n\n directions available include {self.directions}"
    def revealItems(self):
        items = []
        for item in self.items:
            items.append((item.name, f"description {item.description}"))
        return (f"This room includes the following: {items}\n\n")
    def change_room(self, option):
        if option == "n" and self.n_to is not None:
            return self.n_to
        elif option == "s" and self.s_to is not None:
            return self.n_to
        elif option == "w" and self.w_to is not None:
            return self.w_to
        elif option == "e" and self.e_to is not None:
            return self.e_to
        else:
            return None

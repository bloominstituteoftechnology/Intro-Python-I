# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, adjacent):
        self.name = name
        self.description = description
        self.adjacent = adjacent
    def __str__(self):
        return(f'name: {self.name}\n')
    # def NextRoom(self, s_to, n_to, e_to, w_to):
    #     self.s_to = s_to
    #     self.n_to = n_to
    #     self.e_to = e_to
    #     self.w_to = w_to

#     def __repr__(self):
#         return f"name: {self.name}, description: {self.description}"

# r = Room("Outside", "outside")
# f = Room("Foyer", "Dim light filters in from the south")
# t = Room("Foyer", "Dim light filters in from the south")
# # print(isinstance(r, room))
# # print(isinstance(, room))

# r.n_to = f
# f.s_to = r
# r.e_to = t
# t.w_to = r

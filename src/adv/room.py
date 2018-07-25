# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, roomName, description, items):
       self.name = roomName
       self.description = description
       self.items = items
       self.n_to = None
       self.s_to = None
       self.e_to = None
       self.w_to = None

#     # Test Method to print roomName and description 
#     def roomDetails(self):
#         return (f'The {self.name} is {self.description} and the player has {self.items}')

# room_1 = Room('Bathroom', 'Blue', 'knife')

# print(room_1.roomDetails())

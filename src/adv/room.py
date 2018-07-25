# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, roomName, description):
       self.name = roomName
       self.description = description
       self.n_to = None
       self.s_to = None
       self.e_to = None
       self.w_to = None

#     # Method to print roomName and description 
#     def roomDetails(self):
#         return 'The {} is {}'.format(self.roomName, self.description)

# room_1 = Room('Bathroom', 'Blue')

# print(room_1.roomDetails())

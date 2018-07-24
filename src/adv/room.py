# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, roomName, description):
       self.roomName = roomName
       self.description = description

    # Method to print roomName and description 
    def roomDetails(self):
        return 'The {} is {}'.format(self.roomName, self.description)

room_1 = Room('Bathroom', 'Blue')

print(room_1.roomDetails())

# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connectedRooms = {
            'n': None,
            's': None,
            'e': None,
            'w': None
        }
       
        self.enemies = []
    
    def getRoomInfo(self):
        print('Room Name: {}\nDescription: {}\n'.format(self.name, self.description))
        for direction in self.connectedRooms:
            if self.connectedRooms[direction] != None:
                print(direction)
                print('{} is located {}'.format(self.connectedRooms[direction].name, direction))
    
    def connectRoom(self, direction, destinationRoom):
        oppositeDirection = '';
        if direction == 'n':
            oppositeDirection = 's'

        elif direction == 's':
            oppositeDirection = 'n'

        elif direction == 'e':
            oppositeDirection = 'w'

        elif direction == 'w':
            oppositeDirection = 'e'
        
        else:
            print('Please give a room direction')
            return

        self.connectedRooms[direction] = destinationRoom
        destinationRoom.connectedRooms[oppositeDirection] = self.connectedRooms[direction]



room = Room('Foyer', 'It is very dark, scary, and has rotten smells of death.')
room2 = Room('outside', 'The sun shines with its flowers blooming in the fields.')
room.connectRoom('n', room2);


room.getRoomInfo()
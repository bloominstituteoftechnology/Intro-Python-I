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
        directions = {
            'n': 'north',
            's': 'south',
            'e': 'east',
            'w': 'west'
        }
        print('************************************************')
        print('Room Name: {}\nDescription: {}\n'.format(self.name, self.description))
        print('Directions to other rooms:')

        for direction in self.connectedRooms:
            if self.connectedRooms[direction] != None:
                print('{} is {}.'.format(self.connectedRooms[direction].name, directions[direction]))
        
        print('************************************************')
       
    
    def connectRoom(self, to, destinationRoom):
        if self.connectedRooms[to] != None:
            print('{} is {} of {}'.format(self.connectedRooms[to].name, to, self.name))
            return
        oppositeDirection = '';
        if to == 'n':
            oppositeDirection = 's'

        elif to == 's':
            oppositeDirection = 'n'

        elif to == 'e':
            oppositeDirection = 'w'

        elif to == 'w':
            oppositeDirection = 'e'
        
        else:
            print('Please give a valid direction')
            return

        self.connectedRooms[to] = destinationRoom
        destinationRoom.connectedRooms[oppositeDirection] = self


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
        self.items = []
        self.enemies = []
    
    def get_room_info(self):
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
       
    def connect_one_way(self, to, destinationRoom):
        self.connectedRooms[to] = destinationRoom
    
    
    def connect_rooms(self, to, destinationRoom):
        if self.connectedRooms[to] != None:
            print('{} is {} of {}'.format(self.connectedRooms[to].name, to, self.name))
            return
        
        oppositeDirection = {
        'n': 's',
        's': 'n',
        'w': 'e',
        'e': 'w'
        };

        if to in oppositeDirection:
            self.connectedRooms[to] = destinationRoom
            destinationRoom.connectedRooms[oppositeDirection[to]] = self

        else:
            print('Please give a valid direction')
            return

    def add_item(self,item):
        self.items.append(item)



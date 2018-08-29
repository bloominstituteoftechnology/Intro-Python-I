# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, age, height, weight, hp, attack, defense, inventory):
        self.name = name
        self.age = age
        self.height = str(height) + ' centimeters' if height <= 1 else str(height) + ' centimeter'
        self.weight = str(weight) + ' pounds' if weight <= 1 else str(weight) + ' pound'
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.inventory = inventory
        self.currentRoom = None
    
    def __str__(self):
        print('Name: {},\nAge: {},\nHeight: {},\nWeight: {}'.format(self.name, self.age, self.height, self.weight))

    def go_direction(self, direction):
        chosenRoom = self.currentRoom.connectedRooms[direction]

        if chosenRoom == None:
            print('Sorry, there is no room that way')
            return
        self.set_location(chosenRoom)
    
    def check_hp(self):
        print(self.hp)
    
    def get_current_location(self):
        self.currentRoom.getRoomInfo()
    
    def set_location(self, room):
        self.currentRoom = room
    
    def check_inventory(self):
        print(self.inventory)

    @classmethod
    def create_player(cls):

        info = ['Name', 'Age', 'Height in centimeters', 'Weight in pounds']
        enteredInfo = []
        for i in info:
            enteredInfo.append(input(f'{i}:'))
        
        # name, age, height, weight, hp, attack, defense, inventory
        return cls(*enteredInfo, 14, 5, 3, {});
        


# name, age, height, weight, hp, attack, defense, inventory

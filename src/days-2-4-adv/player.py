# Write a class to hold player information, e.g. what room they are in
# currently.
# from player_classes import Knight
import re

def printErrorString(errorString):
    print(f'\x1b[1;31;40m\n{errorString}\x1b[0m\n')

class Player:
    def __init__(self, name, age, height, weight, hp, attack, defense):
        self.name = name
        self.age = age
        self.height = str(height) + ' centimeters' if int(height) > 1 else str(height) + ' centimeter'
        self.weight = str(weight) + ' pounds' if int(weight) > 1 else str(weight) + ' pound'
        self.totalHp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.inventory = {}
        self.currentRoom = None
    
    def __str__(self):
        return f"""
        Name:    {self.name}
        
        Age:     {self.age}
        
        Height:  {self.height}
        
        Weight:  {self.weight}
        
        HP:      {self.totalHp}
        
        Attack:  {self.attack}
        
        Defense: {self.defense}
        
        """

    def go_direction(self, direction):
        chosenRoom = self.currentRoom.connectedRooms[direction]

        if chosenRoom == None:
            printErrorString('Sorry, there is no room that way')
            return
        self.set_location(chosenRoom)
    
    def get_hp(self):
        print('Your current health is {}/{}'.format(self.hp, self.totalHp))
    
    def get_current_location(self):
        self.currentRoom.get_room_info()

    def get_stats(self):
        print(self)

    def set_location(self, room):
        self.currentRoom = room
    
    def get_inventory(self):
        if len(self.inventory) == 0:
            print('No items exist in your inventory')
        else:
            print(self.inventory)
    
    def change_class(self):
        pass

    def look_for_items(self):
        if len(self.currentRoom.items) == 0:
            print('No items were discovered')
        for item in self.currentRoom.items:
            print(f'Item: {item.name}')
    
    @classmethod
    def create_player(cls):

        enteredInfo = {
            'name': '',
            'age': 0,
            'height': 0,
            'weight': 0,
        }
        for key in enteredInfo:
            while(True):
                userInput = input(f'{key.upper()}:')
                
                dataType = type(enteredInfo[key])
                if dataType == int:
                    pattern = re.compile(r'[a-z]', re.I)
                    if re.search(pattern, userInput):
                        print(f'Please enter a valid number for {key}')
                        continue
                    else:
                        enteredInfo[key] = int(userInput)
                        break
                else:
                    enteredInfo[key] = userInput
                    break
        
        # default stats
        enteredInfo['hp'] = 15
        enteredInfo['attack'] = 5
        enteredInfo['defense'] = 4

        return cls(**enteredInfo);
        


# name, age, height, weight, hp, attack, defense, inventory

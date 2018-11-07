# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []
        self.score = 0
        self.equiped_items = []
        self.max_health = 20
        self.health = self.max_health
        self.attack = 0
        self.defense = 0
    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            light_sources = [item for item in self.items if item.lightsource]
            light = nextRoom.light or len(light_sources) > 0
            if light:                
                print(nextRoom)
            else:
                print("It is too dark to see.")
        else:
            print("You cannot move that way.")
    def look(self, direction = None):
        if direction is None:
            light_sources = [item for item in self.items if item.lightsource]
            light = self.currentRoom.light or len(light_sources) > 0
            if light:
                print(self.currentRoom)
            else:
                print("It is too dark to see.")
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None: 
                light_sources = [item for item in self.items if item.lightsource]
                light = nextRoom.light or len(light_sources) > 0
                if light:                
                    print(nextRoom)
                else:
                    print("It is too dark to see.")
            else:
                print("There is nothing there.")
    def printInventory(self):
        print("Equipped:\n")
        for item in self.equiped_items:
            print(f"    {item.name}\n")
        print("Backpack:\n")
        for item in self.items:
            print(f"    {item.name}\n")
    def printStats(self):
        print(f"Name: {self.name}\nHealth: {self.health}\nAttack: {self.attack}\nDefense: {self.defense}")
    def addItem(self, item):
        if hasattr(item, 'treasure'):
            self.items.append(item)
            if not item.collected:
                item.collected = True
                self.score += item.value
                print(f"You have gained {item.value} points!")
        else:
            self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def findItembyName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        for item in self.equiped_items:
            if item.name.lower() == name.lower():
                return item
        return None
    def equipItem(self, item):        
        self.equiped_items.append(item)
        if hasattr(item, 'attack'):
            self.attack = item.attack
        if hasattr(item, 'defense'):
            self.defense = item.defense
    def unequipItem(self, item):        
        self.equiped_items.remove(item)
        if hasattr(item, 'attack'):
            self.attack = self.attack - item.attack
        if hasattr(item, 'defense'):
            self.defense = self.defense - item.defense
# Write a class to hold player information, e.g. what room they are in
# currently.

from item import itemList

class Player:
    def __init__( self, name, location, items):
        self.location = location
        self.name = name
        self.items = list(items)

    def change_location(self, new_location):
        self.location = new_location

    def player_inventory(self):
        if len(self.items) == 0:
            print("No items available") 
        elif len(self.items) >= 1:
            item_list = "\n"
            for item in self.items:
                item_list += f"{item.name}\n"            
            print(f"\033[94m\nPlayer's Inventory:{item_list}\033[0m") 
            input("Press Enter to Exit Inventory")
    def move(self, input):
        newRoom = self.location.getRoomInDirection(input)
        if newRoom == None:
            print(f"\x1b[1;31;40m\nYou cannot move in that direction\x1b[0m")
        else:
            self.change_location(newRoom)
    def get(self, input):
        if not input:
            print("Select an item, dumbass")
        else:
            if input.lower() in list(map(lambda item : item.name.lower() , self.location.items)):
                print('Item added to inventory!')
                self.items.append(itemList[input])
                self.location.items.remove(itemList[input])
            else:
                print("No Item by that name")

    def drop(self, input):
        if not input:
            print("Select an item, dumbass")
        else:
            if input.lower() in list(map(lambda item : item.name.lower() , self.items)):
                print('Item dropped from inventory!')
                self.items.remove(itemList[input])
                self.location.items.append(itemList[input])
            else:
                print("No Item by that name")
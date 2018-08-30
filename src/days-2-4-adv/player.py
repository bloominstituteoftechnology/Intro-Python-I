# Write a class to hold player information, e.g. what room they are in
# currently.

from item import itemList
from item import LightSource

class Player:
    def __init__( self, name, location, items, score=0):
        self.location = location
        self.name = name
        self.items = list(items)
        self.score = score

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

    def inspect(self, item):
        if not item:
            print("Select an item, dumbass")
        elif item.lower() in list(map(lambda item : item.name.lower() , self.location.items + self.items)):
            print("Name: {}\nDescription: {}".format(itemList[item].name, itemList[item].description))
            if hasattr(itemList[item], 'value'):
                print("\nValue: {}".format(itemList[item].value))
            input("Press Enter to exit description")
        else:
            print("Man, I don't know what you're talking about")

    def move(self, input):
        newRoom = self.location.getRoomInDirection(input)
        if newRoom == None:
            print(f"\x1b[1;31;40m\nYou cannot move in that direction\x1b[0m")
        else:
            self.change_location(newRoom)
    def get(self, input):
        if not input:
            print("Select an item, dumbass")
        elif self.location.is_Light == False:
            print("Good luck finding that in the dark!")
        else:
            if input.lower() in list(map(lambda item : item.name.lower() , self.location.items)):
                itemList[input].on_take()
                if hasattr(itemList[input], 'value'):
                    self.score += itemList[input].value
                    self.items.append(itemList[input])
                    self.location.items.remove(itemList[input])
                else:
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
                if hasattr(itemList[input], 'value'):
                    self.score -= itemList[input].value
                    self.items.remove(itemList[input])
                    self.location.items.append(itemList[input])
            else:
                print("No Item by that name")

    def get_score(self):
        print(f"\nCurrent Score: {self.score}")

"""
    Author: Eric gomez
    Text based adventure game in python.
"""


class Player(object):

    def __init__(self, name='Default', location=None, size=8):
        self.name = name
        self.health = 100
        self.fatigue = 0
        self.location = location
        self.inventory = {i: None for i in range(1, size + 1)}

    def __str__(self):
        return "Name: " + self.name + "\n" + "Health: " + str(self.health) + "\n" + "Fatigue: " + str(self.fatigue)

    def can_move(self):
        if self.fatigue < 100:
            self.fatigue += 10
            return True
        else:
            print("Cannot move, player is fatigue'd")
            return False

    def wait(self):
        if self.fatigue > 0:
            self.fatigue -= 10
        else:
            print("player is fully rested.")

    def check_map(self):
        print("North: " + (self.location.north.name if self.location.north else "Nothing.") +
              "\nSouth: " + (self.location.south.name if self.location.south else "Nothing.") +
              "\nEast: " + (self.location.east.name if self.location.east else "Nothing.") +
              "\nWest: " + (self.location.west.name if self.location.west else "Nothing."))

    def show_inventory(self):
        print("you pull your pack out and look at the contents inside:\n" + str(self.inventory))

    def pick_up(self, loc_index, bag_index):
        if self.location.items[loc_index] and (len(self.inventory) >= bag_index > 0):
            self.inventory[bag_index] = self.location.items[loc_index]
            del self.location.items[loc_index]
        else:
            print("invalid object or spot in your bag.")

    def drop_item(self, bag_index):
        if self.inventory[bag_index]:
            if self.location.items.keys():
                self.location.items[len(self.location.items.keys()) + 1] = self.inventory[bag_index]
                print("you have dropped" + self.inventory[bag_index].name)
                self.inventory[bag_index] = None
            else:
                self.location.items[1] = self.inventory[bag_index]
                print("you have dropped " + self.inventory[bag_index].name)
                self.inventory[bag_index] = None



if __name__ == "__main__":
    print("This is a module for the main adventure_py file. Do not directly run this.")
    input("\n\nPress the enter key to exit.")
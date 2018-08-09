# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items ):
        self.name = name
        self.description = description
        self.items = items
        self.is_light = False

    def room_items(self):
        print("Items that can be taken in this room are... \n")
        if len(self.items) == 0:
            print("Nothing here!")
        else:
            for item in self.items:
                print(item,"\n")
            return item
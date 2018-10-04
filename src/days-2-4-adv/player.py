# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def sayName(self):
        return self.name

    def getCurrentRoom(self):
        return self.current_room

    def setCurrentRoom(self, room):
        self.current_room = room

    def pickUpItem(self, item):
        if item:
            self.inventory.append(item)
            print(f"You have picked up the {item.getItemType()}")

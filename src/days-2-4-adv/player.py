# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, room):
        self.room = room
        self.items = []
    def set_room(self, room):
        self.room = room
    def drop_item(self, item_name):
        index = 0
        for item in self.items:
            if item.name.upper() == item_name.upper():
                dropped = self.items.pop(index)
                return dropped
            index += 1
        return None
    def show_inventory(self):
        if len(self.items) == 0:
            print("\nYou having nothing on you.")
        else:
            print("\nYou have the following items:")
            for item in self.items:
                print(f"{item.name.upper()} - {item.description}")
    def __getitem__(self, key):
        return getattr(self, key)

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current):
        self.name = name
        self.current = current
        self.inventory = []

    def move_to(self, room):
        if room:
            self.current = self.current.to_new(room)
        else:
            print("You can't go that way.")

    def populate_inventory(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\n===In your inventory: ")
        for item in self.inventory:
            print(f"{item.name} - {item.desc}")

    def add_item(self, item):
        searched_item = list(
            filter(lambda x: x.name.lower() == item.lower(), self.current.items)
        )
        self.inventory.append(searched_item[0])
        self.current.items.remove(searched_item[0])
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"\n===You grabbed {item}.")

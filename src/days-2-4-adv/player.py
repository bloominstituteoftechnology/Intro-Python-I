# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current, score=0):
        self.name = name
        self.current = current
        self.inventory = []
        self.score = score

    def move_to(self, room):
        if room:
            self.current = self.current.to_new(room)
        else:
            print("You can't go that way.")

    def populate_inventory(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\n===Your inventory: ")
        for item in self.inventory:
            print(f"{item.name} - {item.desc}")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def add_item(self, item):
        searched_item = list(
            filter(lambda x: x.name.lower() == item.lower(), self.current.items)
        )
        if len(searched_item) == 0:
            print("Item not found.")
        else:
            self.inventory.append(searched_item[0])
            self.current.items.remove(searched_item[0])
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"\n===You got {item}.")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def remove_item(self, item):
        targeted_item = list(
            filter(lambda x: x.name.lower() == item.lower(), self.inventory)
        )
        if len(targeted_item) == 0:
            print("Item not found.")
        else:
            self.current.items.append(targeted_item[0])
            self.inventory.remove(targeted_item[0])
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"\n===You dropped {item}.")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def show_score(self):
        print(self.score)

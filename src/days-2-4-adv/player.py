# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current, score=0):
        self.name = name
        self.current = current
        self.score = score
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
            if hasattr(searched_item[0], "value") and not searched_item[0].scored:
                self.score += searched_item[0].value
            searched_item[0].on_take()
            self.inventory.append(searched_item[0])
            self.current.items.remove(searched_item[0])

    def remove_item(self, item):
        targeted_item = list(
            filter(lambda x: x.name.lower() == item.lower(), self.inventory)
        )
        if len(targeted_item) == 0:
            print("Item not found.")
        else:
            if (
                hasattr(targeted_item[0], "value")
                and targeted_item[0].scored
                and not targeted_item[0].deducted
            ):
                self.score -= targeted_item[0].value
            targeted_item[0].on_drop()
            self.current.items.append(targeted_item[0])
            self.inventory.remove(targeted_item[0])

    def show_score(self):
        print(self.score)

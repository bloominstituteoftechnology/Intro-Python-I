

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

    def on_drop(self):
        print(f"You have dropped {self.name}.")


class Food(Item):
    def __init__(self, name, description, calories):
        Item.__init__(self, name, description)
        self.calories = calories

    def eat(self):
        return self.calories

    def on_drop(self):
        print(
            f"You have dropped {self.name}.\nIt's not nice to play with your food!")


class Egg(Food):
    def __init__(self):
        self.name = "Egg"
        self.description = "This is an egg."
        self.calories = 50

    def eat(self):
        return 0

    def on_drop(self):
        self.name = "Broken Egg"
        self.description = "This is a broken egg."
        print(f"You have dropped an egg and now it's broken.")

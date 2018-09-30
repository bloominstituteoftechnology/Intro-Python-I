

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"\n**{self.name}**\n{self.description}\n"


class Weapon(Item):
    def __init__(self, name, description, damage):
        Item.__init__(self, name, description)
        self.damage = damage

    def __str__(self):
        return f"\n**{self.name}**\n{self.description},  \nDamage: {self.damage}\n"


class LightSource(Item):
    def __init__(self, name, description, light):
        Item.__init__(self, name, description)
        self.light = light

    def __str__(self):
        return f"\n**{self.name}**\n{self.description},  \nLight: {self.light}\n"


class Food(Item):
    def __init__(self, name, description, meals, calories):
        Item.__init__(self, name, description)
        self.meals = meals
        self.calories = calories

    def __str__(self):
        return f"\n**{self.name}**\n{self.description}, \nMeals: {self.meals}, \nCalories: {self.calories}\n"

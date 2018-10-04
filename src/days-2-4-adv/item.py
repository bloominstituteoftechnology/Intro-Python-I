# Add an Item class in a file item.py.
# This will be the base class for specialized item types to be declared later.
#The item should have name and description attributes.
#Hint: the name should be one word for ease in parsing later.

# base class
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    

# class Weapon(Item):
#     # Weapon that increases the players power score upon picking up
#     def __init__(self, name, description, value):
#         self.value = value
#         self.was_picked_up = False
#         super().__init__(name, description)
#     # pass in the player and if was picked up add the value of the item to the players power
#     def take_item(self, player):
#         super().take_item(player)
#         if not self.was_picked_up:
#             player.power += self.value
#             print(f"You just got {self.value} power points.")
#             self.was_picked_up = True
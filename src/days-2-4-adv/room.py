# Implement a class to hold room information. This should have name and
# description attributes.
from item import item

items = {
   'sword': Item("Sword", """Double-edged, and guilded"""),

    'pen': Item("Pen", """The pen is mightier than the sword"""),

    'axe': Item("Axe", """Axe first, take names later""")
}



class Room():
    def __init__(self, name. description)
    self.name = name
    self.description = description
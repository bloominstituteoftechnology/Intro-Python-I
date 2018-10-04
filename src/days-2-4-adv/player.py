# Write a class to hold player information, e.g. what room they are in
# currently.


items = {
    'sword': Item("Sword", """Double-edged, and guilded"""),

    'pen': Item("Pen", """The pen is mightier than the sword"""),

    'axe': Item("Axe", """Axe first, take names later""")
}




class Player:
    def __init__(self, inRoom):
        self.inRoom = inRoom
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, currentRoom, items=None):
        self.name = name
        self.health = 100
        self.mana = 50
        self.score = 0
        self.currentRoom = currentRoom
        self.badMove = '==You abruptly realize it is impossible to continue in this direction, turn around, and stride confidently back from whence you came.=='
        self.items = [items]

    def __str__(self):
        return f'\nPlayer Name: {self.name}\nRoom: {self.currentRoom.name}\nHealth: {self.health} - Mana: {self.mana} - Score: {self.score} - Items: {self.items}'

    def playerMove(self, direction):
        if direction == 'n':
            self.currentRoom = self.currentRoom.n_to
        elif direction == 's': 
            self.currentRoom = self.currentRoom.s_to
        elif direction == 'e': 
            self.currentRoom = self.currentRoom.e_to
        elif direction == 'w': 
            self.currentRoom = self.currentRoom.w_to
    
    def playerGet(self, item):
        if hasattr(item, 'points'):
            self.score += item.points 
        else: 
            pass

        if self.items == [None]:
            self.items.append(item)
            self.items.pop(0)
        else:
            self.items.append(item)
        print(f"\n== You pick up the {item.name.upper()} and stuff it joyfully in your sack.")
    
    def playerDrop(self, item):
        if self.items == [None]:
            print(f"\n== There is nothing to drop from your sack except for your imagination. ==")
        else:
            self.items.remove(item)
        print(f"\n== With a glimmer of zenful madness in your eyes, you take the {item.upper()} out of your sack and drop it on the ground. ==")        







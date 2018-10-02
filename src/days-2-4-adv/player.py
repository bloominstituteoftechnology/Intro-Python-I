# Write a class to hold player information, e.g. what room they are in
# currently.


class Player(object):
    def __init__(self, name, currentRoom, roomKey):
        self.name = name
        self.currentRoom = currentRoom
        self.roomKey = roomKey
        self.items = []

    def __repr__(self):
        return f"{self.name} currently in room {self.currentRoom}"

    def room_change(self, room):
        if room == "Outside Cave Entrance":
            self.roomKey = "outside"
        elif room == "Foyer":
            self.roomKey = "foyer"
        elif room == "Grand Overlook":
            self.roomKey = "overlook"
        elif room == "Narrow Passage":
            self.roomKey = "narrow"
        elif room == "Treasure Chamber":
            self.roomKey = "treasure"
        elif room == "Prison":
            self.roomKey = "prison"
        elif room == "Cowards Forest":
            self.roomKey = "coward"
        elif room == "Kitchen":
            self.roomKey = "kitchen"
        
        self.currentRoom = room

        return "Changing rooms..."

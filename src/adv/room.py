# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room_name = "", room_description = ""):
        self.room_name = room_name
        self.room_description = room_description

    def __repr__(self):
        return "{} \nRoom Description: {}".format(self.room_name, self.room_description)

    def __str__(self):
        return "{} \nRoom Description: {}".format(self.room_name, self.room_description)

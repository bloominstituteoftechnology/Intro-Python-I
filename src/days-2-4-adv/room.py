# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    # this specifies that is returned if you call << print (player.current_room) >>
    # rather than return all the attributes above
    def __str__(self):
        return self.name
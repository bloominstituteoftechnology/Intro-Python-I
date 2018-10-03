# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = ""
        self.s_to = ""
        self.w_to = ""
        self.e_to = ""




"""
# A given room object
example = {
    name: 'chuckecheese',
    description: 'cheesist place on earth',
    n_to: <Room Disneyland>
    s_to: <Room Zoo>
    w_to: ""
    e_to: <Room Knotts>
}
"""
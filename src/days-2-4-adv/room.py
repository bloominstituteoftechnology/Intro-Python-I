# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, location, message):
        self.location = location
        self.message = message
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __repr__(self):
        return f"location: {self.location}, message: {self.message}"


# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        # print(f"Name: {self.name}, description: {self.description}")
        return "Name: {name}, description: {description}".format(name = self.name, description = self.description)

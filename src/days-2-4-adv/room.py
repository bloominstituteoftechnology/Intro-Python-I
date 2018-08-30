# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, light):
        self.name = name
        self.description = description
        self.items = []
        self.isLight = light

    def getDescription(self):
        return ("{}.\n{}.".format(self.name, self.description))

    def showItems(self):
        message = "{} contains: ".format(self.name)
        print(message)
        for item in self.items:
            print(item.name)

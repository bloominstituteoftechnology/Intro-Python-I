# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, contents):
        self.name = name
        self.description = description
        self.contents = contents

    def printName(self):
        print(self.name)

    def printDescription(self):
        print(self.description)

    def printContents(self):
        if len(self.contents) > 0:
            print('The room contains...')
            for item in self.contents:
                print(item.name + '--' + item.description)
        else:
            print('The room contains no items.')
# Add an Item class
# with name and description attributes..

class Items:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def __repr__(self):
    return f"{self.name} - {self.description}"
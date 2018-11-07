class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    # Return a formatted value of the Item class
    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}"

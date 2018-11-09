class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"name: {self.name}"

    def get_item(self):
        return self.name

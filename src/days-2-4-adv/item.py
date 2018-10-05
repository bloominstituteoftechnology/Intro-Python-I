class Item():
    def __init__(self, name, description, points):
        self.name = name
        self.description = description
        self.points = points
    def __repr__(self):
        return f"{self.name}, {self.description}"
    def on_drop(self):
        print(f"You dropped {self.name}.")
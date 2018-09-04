class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def on_take(self):
        print(f"You take the {self.name}.")
        return None
    def on_drop(self):
        print(f"You dropped the {self.name}.")
        return None
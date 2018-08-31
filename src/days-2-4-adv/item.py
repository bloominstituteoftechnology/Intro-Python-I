class Item:
    def __init__(self, name):
        self.name = name        
    def __repr__(self):
        return f"{self.name}"
    # def __str__(self):
    #     return f"{self.name}"
    def on_drop(self):
        print(f"You dropped {self.name}")
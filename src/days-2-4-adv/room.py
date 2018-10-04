

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
    
    def __str__(self):
        return f'\n== You find yourself in the {self.name}. {self.description} ==\n\n=='
    
    def addItems(self, item):
        self.items.append(item)

    def examine(self):
        if len(self.items) > 0:
            print(f'\n== You find yourself in the {self.name}. {self.description} ==\n')
            for item in self.items:
                print(f'== You see a {item.name}! {item.description} ==')
        else:
            print(f'\n== You find yourself in the {self.name}. {self.description} ==\n\n== There are no items in this room. ==')

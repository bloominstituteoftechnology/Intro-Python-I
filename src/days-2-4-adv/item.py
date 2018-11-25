class Item:
    def __init__(self, name, description, keyword):
        self.name = name
        self.description = description
        self.keyword = keyword
        self.shape = 'square'
        color = 'red'

    def __str__(self):
        return self.name
    
    def on_take(self, player, item):
        print ('on_take is running')

    def on_drop
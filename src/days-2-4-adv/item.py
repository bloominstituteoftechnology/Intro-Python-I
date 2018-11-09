class Item:
    def __init__(self, name, description, keyword):
        self.name = name
        self.description = description
        self.keyword = keyword
        self.shape = 'square'
        self.color = 'red'

    def __str__(self):
        return self.name

    def on_take(self, player, item):
        print ('On Take Running')
    
    def on_drop(self):
        print ('On Drop Running')

class Treasure(Item):
    def __init__(self, name, description, keyword, value, other_attributes):
        super().__init__(name, description, keyword)
        self.value = value

    def on_take(self, player, item):
        print ('On_take - treasure running')
        if item.keyword not in player.items_grabbed:
            player.score += item.value
            player.items_grabbed.append(item.keyword)
        print ('Your score:', player.score)
    
    def on_drop(self, player, item):
        print ('On_drop - treasure running')
        player.score -= item.value
        player.items_grabbed.append(item.keyword)
        print ('Your score:', player.score)

class LightSource(Treasure):
    def __init__(self, name, description, keyword, value):
        super().__init__(name, description, keyword, value)

    def on_drop(self, player, item):
        print ("It's not wise to drop your source of light")

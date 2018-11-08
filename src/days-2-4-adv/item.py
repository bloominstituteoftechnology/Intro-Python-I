class Item:
    def __init__(self, name, description, keyword):
        self.name = name
        self.description = description
        self.keyword = keyword

    def __str__(self):
        return self.name

    def on_take(self):
        print ('On Take Running')

class Treasure(Item):
    def __init__(self, name, description, keyword, value):
        super().__init__(name, description, keyword)
        self.value = value

    def on_take(self, player, item):
        print ('On_take - treasure running')
        if item.keyword not in player.items_grabbed:
            player.score += item.value
            player.items_grabbed.append(item.keyword)
        print (player.score)

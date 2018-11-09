
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, player):
        pass
    
    def on_drop(self, player):
        pass

class Treasure(Item):
    def __init__(self, name, description, value, pickedup_players = []):
        super().__init__(name, description)
        self.name = name
        self.description = description
        self.value = value
        self.pickedup_players = pickedup_players
    
    def on_take(self, player):
        if not player.name in self.pickedup_players:
            player.score += self.value
            self.pickedup_players.append(player.name)

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name,description)
        self.name = name
        self.description = description

    def on_drop(self):
        print("It's not wise to drop your source of light!")
    
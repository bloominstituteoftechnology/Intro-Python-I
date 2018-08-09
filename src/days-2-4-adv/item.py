class Item:
    def __init__( self, name, description ):
        self.name = name
        self.description = description

    def __str__( self ):
        return self.name + ": " + self.description

    def on_grab( self, player ):
        print("\nGrabbed item!\n")
        player.items.append(self)
        player.room.items.remove(self)

class Treasure(Item):
    def __init__( self, name, description, value ):
        super().__init__( name, description )
        self.value = value
        self.grabbed_treasure = False

    def on_grab( self, player ):
        super().on_grab( player )
        if self.grabbed_treasure == False:
            player.score += self.value
            self.grabbed_treasure = True

class LightSource(Item):
    def __init__( self, name, description ):
        super().__init__( name, description )
        self.lightsource = True


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @classmethod
    def on_take(cls):
        print('\n\n&&&&& thx  adventurous, Item is Picked up   &&&&&&& ')

    @classmethod
    def on_drop(cls):
        print('\n\n&&&&& thx  adventurous, Item is dropped of    &&&&&&& ')


class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

    def on_take(self):
        return self.value


class LightSource(Item):

    def __init__(self, name, description, light):
        super().__init__(name, description)
        self.light = False

    def lighting(self):
        self.light = True

    def on_drop(self):
        print('Its not wise to drop your source of light!')


# b=Treasure('fill', 'tall', 89)


# # print(b.value)
# # print(b.name)
# d=getattr(b, "value")
# print(d)
# # # print(Item.on_take())
# # print(b.on_take())

from item import LightSource

# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, c_room):
        self.c_room = c_room
        self.items = []
        self.score = 0

    def update_room(self, dir):
        n_room = self.c_room.get_room(dir)
        if n_room is not None:
          self.c_room = n_room
          if self.c_room.is_light is False and self.has_light_item() is False:
            print("It's pitch black in this room.")
          else:
            print(self.c_room)

    def look(self, dir=None):
      if dir is None:
        self.c_room.examine(self.has_light_item())
      else:
        n_room = self.c_room.get_room(dir)
        if n_room is not None:
          print(n_room)
        else:
          print("There is no room there")

    def list_items(self):
      if len(self.items) > 0:
        print('You are currently carrying: ')
        for item in self.items:
          print(item)
      else:
        print("You are not currently carrying anything, try (look)ing for items in rooms")

    def take_item(self, i_name):
      if self.c_room.is_light is False and self.has_light_item() is False:
        print("Good luck finding that in the dark!")
      else:
        if len(self.c_room.items) > 0:
          item = list(filter(lambda i: i.name.lower() == i_name, self.c_room.items))
          if len(item) > 0:
            self.items.append(item[0])
            self.c_room.items.remove(item[0])
            print(item[0].on_take(self))
          else:
            print("There is no such item in this room")
        else:
          print('There is no item in this room worth taking')

    def drop_item(self, i_name):
      if len(self.items) > 0:
        item = list(filter(lambda i: i.name.lower() == i_name, self.items))
        if len(item) > 0:
          self.c_room.add_item(item[0])
          self.items.remove(item[0])
          print(item[0].on_drop())
        else:
          print("You don't have an item by that name")
      else:
        print("You're not holding any items")

    def has_light_item(self):
      return any(isinstance(item, LightSource) for item in self.items)

    def add_score(self, score):
      self.score += int(score)

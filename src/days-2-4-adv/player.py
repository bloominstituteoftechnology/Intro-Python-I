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
          print(n_room)

    def look(self, dir=None):
      if dir is None:
        print(self.c_room)
      else:
        n_room = self.c_room.get_room(dir)
        if n_room is not None:
          n_room.examine()
        else:
          print("There is no room there")

    def list_items(self):
      if len(self.items) > 0:
        print('You are currently carrying: ')
        for item in self.items:
          print(item)
      else:
        print("You are not currently carrying anything, try (look)ing for items in rooms")

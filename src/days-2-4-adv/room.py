# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
        def __init__(self, name, description):
            self.name=name
            self.description= description
            self.inventory = {
                'apple': 1
            }
        def __str__(self):
          return(f'name: {self.name}\n')
        def take(self, item):
          for key in self.inventory:
              if key == item:
                  self.inventory[key] += 1
                  return
          self.inventory[item] = 1
        def drop(self, item):
          for key in self.inventory:
              if key == item:
                  if self.inventory[key] > 0:
                    self.inventory[key] -= 1
                    return
          print("Nothing to get!")
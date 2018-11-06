class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description
  def __str__(self):
    return str(f"{self.name}")

class Treasure(Item):
  def __init__(self, name, description, score_amount):
    super().__init__(name, description)
    self.score_amount = score_amount
    self.has_scored = False
  def check_scored(self):
    if self.has_scored == False:
      self.has_scored = True
      return False
    else:
      return True
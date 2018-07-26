# Implement a class to hold item information. This should have name and
# description attributes.

class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description


# Create all the items

item = {
  'lever': Item('lever', """It looks as though it was broken off at the base.
Maybe it goes to something."""),
}
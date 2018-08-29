# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, in_room, hair_color, eye_color, gender, build):
    self.name = name
    self.in_room = in_room
    self.hair_color = hair_color
    self.eye_color = eye_color
    self.gender = gender
    self.build = build
# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
	def __init__(self, name, curRoom, inventory):
		self.name = name
		self.room = curRoom
		self.items = inventory



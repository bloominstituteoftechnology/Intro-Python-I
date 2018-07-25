# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
	def __init__(self, playername, room):
		self.room = room
		self.inventory = []
		self.name = playername
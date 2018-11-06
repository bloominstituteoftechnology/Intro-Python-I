# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
	def __init__ (self,name):
		self.room = "cheesy beginnings"
		self.name = name

	def __str__ (self):
		return"{}, currently in room {}".format(self.name, self.room)
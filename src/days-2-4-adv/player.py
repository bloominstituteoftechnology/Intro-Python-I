# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
	def __init__(self, name):
		self.name = name
		self.current_room = 'laboratory'

	def sayName(self):
		return self.name
	
	def getCurrentRoom(self):
		return self.current_room

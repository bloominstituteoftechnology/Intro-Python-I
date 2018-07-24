# Write a class to hold player information, e.g. what room they are in
# currently.

class player:
	def __init__(self):
		self.name = ''
		self.hp = 0
		self.mp = 0
		self.status_effects = []
		self.room = 'outside'
myPlayer = player()


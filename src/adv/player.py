# Write a class to hold player information, e.g. what room they are in
# currently.

class player:
	def __init__(self, playerName, currentRoom):
		self.name = playerName
		self.currentRoom = currentRoom

	def __str__(self):
  		return '{} is in the {}'.format(self.playerName, self.currentRoom)

myPlayer = player()


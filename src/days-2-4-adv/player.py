# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
	def __init__(self, room, items):
		self.room = room
		self.items = items

	def get_item(self, item):
		return self.items.append(item)

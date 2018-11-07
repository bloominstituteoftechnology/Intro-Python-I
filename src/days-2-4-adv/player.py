# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
	def __init__(self, room, items):
		self.room = room
		self.items = items

	def get_item(self, item):
		return self.items.append(item)

	def view_items(self):
		if len(self.items) > 0:
			print('Your inventory:')
			for item in self.items:
				print(' ' + item.description[0].upper() + item.description[1:].lower())
		else:
			print('No items in your inventory.')

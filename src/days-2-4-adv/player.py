# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
	def __init__(self,name,location, inventory = []):
		self.name = name
		self.location = location
		self.inventory = inventory

	def try_move(self, direction):
		d = direction + "_to"

		next_move = getattr(self.location, d)

		if not next_move:
			input("You can't go that way! Press Enter to continue")
			return self.location
		else:
			self.location = next_move

	def pickup_item(self, item):
		if item in self.location.items:
			self.inventory.append(item)
			self.location.items.remove(item)
		else:
			print(f"There is no {item} to take! Press Enter to continue")

	def drop_item(self, item):
		if item in self.inventory:
			self.inventory.remove(item)
			self.location.items.append(item)
		else:
			input(f"You don't have this item to drop! Press Enter to continue")
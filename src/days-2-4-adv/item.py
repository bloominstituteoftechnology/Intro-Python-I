class Item:
	def __init__(self, name, description):
		self.name = name
		self.description = description
	
	def on_take(self, player, print_wrapped_lines):
		print_wrapped_lines(f'You placed {self.description} in your inventory.')

class Treasure(Item):
	def __init__(self, name, description, value):
		Item.__init__(self, name, description)
		self.value = value

	def on_take(self, player, print_wrapped_lines):
		if self.value != 0:
			setattr(player, 'score', player.score + self.value)
			print_wrapped_lines(f'You placed {self.description} in your inventory. Your score increased by {self.value} points. You now have {player.score} total points.')
			self.value = 0
		else:
			print_wrapped_lines(f'You placed {self.description} in your inventory. You\'ve picked this up before. Your score remains at {player.score} points.')

	def on_drop(self, print_wrapped_lines):
		print_wrapped_lines('Why would you get rid of a treasure?')

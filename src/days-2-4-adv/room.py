# Implement a class to hold room information. This should have name and
# description attributes.
import random


class Room:
	def __init__(self, room_type, room_descr):
		self.self = self
		self.room_type = room_type
		self.room_descr = room_descr

	def getRoomType(self):
		return self.room_type
	
	def getRoomDescription(self):
		return self.room_descr

	


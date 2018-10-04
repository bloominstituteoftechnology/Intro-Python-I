# Implement a class to hold room information. This should have name and
# description attributes.
import random


class Room:
# notAMove = f"That is not a room adjoined to this one"
	def __init__(self, room_type, room_descr):
		self.room_type = room_type
		self.room_descr = room_descr
		self.room_moves = {}
		self.room_item = None

	def setRoomMoves(self,moves):
		self.room_moves = moves

	def getRoomType(self):
		return self.room_type
	
	def getRoomDescription(self):
		return self.room_descr

	def getRoomMoves(self):
		for room in self.room_moves:
			return room

	def checkIfRoomMove(self,cmd):
		return self.room_moves[cmd] if (cmd in self.room_moves) else False	
	
	def getRoomItem(self):
		return self.room_item

	def setRoomItem(self, item):
		self.room_item = item

	


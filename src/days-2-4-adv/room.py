# Implement a class to hold room information. This should have name and
# description attributes.
import random


class Room:
	def __init__(self, room_type, room_descr, room_moves):
		self.room_type = room_type
		self.room_descr = room_descr
    self.room_moves = room_moves
  
  notAMove = f"That is not a room adjoined to {self.room_type}"

	def getRoomType(self):
		return self.room_type
	
	def getRoomDescription(self):
		return self.room_descr
  
  def getRoomMoves(self):
    print(self.room_moves)
    return self.room_moves

  def getNextRoom(self, cmd):
  
  def checkIfRoomMove(self,cmd):
    for next in room_moves:
      return room_moves[cmd] if (cmd in room_moves) else notAMove



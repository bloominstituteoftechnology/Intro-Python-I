# Implement a class to hold room information. This should have name and
# description attributes.
import random


class Room:
	def __init__(self, room_type, room_descr):
		self.self = self
		self.room_type = room_type
		self.room_descr = room_descr
    self.room_moves = room_moves

	def getRoomType(self):
		return self.room_type
	
	def getRoomDescription(self):
		return self.room_descr
  
  def getRoomMoves(self):
    print(self.room_moves)
    return self.room_moves

  # def detectMove(self, room, cmd):
	# if cmd == 'f' or 'b' or 'l' or 'r':
	# 	if cmd == room.f_to:
	# 		return f
	# 	elif cmd == b:
	# 		return b_to
	# 	elif cmd == l:
	# 		return l_to
	# 	elif cmd == r:
	# 		return r_to
	# else:
	# 	print(f'{cmd} is not an optional command.')

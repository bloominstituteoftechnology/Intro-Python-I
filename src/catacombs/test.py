## Create a function that can build the world map
# Map is 25 rooms in a grid, though not every room has to connect to all its other rooms.
# Every room must connect to another room. Every room must be reachable from start room.
# Exit room must only be reachable from 1 room.
# Monster room must be at least 4 rooms from the starting room.
# Starting room must have at least 2 exits.
from room import Room
from catacomb_setup import roomDescriptions, monsterStartRoom, exitDescription, startingDescription, monsters
from character import Player, Monster
# room {
# start : startingDescription
# exit : exitDescription
# monsterStart : monsterStartDescription
# 1 : randomDescipt
# 2 : randomDescipt
# 3 : randomDescipt
## etc. }
#
#room.exits = {n: room, e: room}
#
import random
import math
numRegularRooms = len(roomDescriptions)

def addExit(room, roomList):
   roll = random.randint(1, 10)
   connections = len(room.exits)
   #dont add more than 3 exits
   if connections > 3: pass

   elif roll == 2 or connections == 0:
      #make one exit
      makeExit(room, roomList)


def checkExits(room):
   return room.exits

def freeExits(exitList, opposite = False):
   #returns a list of chars representing available exits
   freeExits = []
   alreadyExits = exitList.keys()
   if opposite is False:
      if "n" not in alreadyExits : freeExits.append("n")
      if "e" not in alreadyExits : freeExits.append("e")
      if "s" not in alreadyExits : freeExits.append("s")
      if "w" not in alreadyExits : freeExits.append("w")
   else:
      if "n" not in alreadyExits : freeExits.append("s")
      if "e" not in alreadyExits : freeExits.append("w")
      if "s" not in alreadyExits : freeExits.append("n")
      if "w" not in alreadyExits : freeExits.append("e")
   return freeExits

def makeExit(room, roomList):
   nextRoomKey = room.key
   myFreeExits = freeExits(room.exits)
   while nextRoomKey == room.key or len(checkExits(roomList[nextRoomKey])) > 3 or any(False for x in myFreeExits if x in freeExits(roomList[nextRoomKey].exits, True)): #make sure next room doesnt already have 4 exits
      #make sure next room's free entrance match this room's free exit
      nextRoomKey = random.randint(0,numRegularRooms - 1)
   
   #find the matching exit/entrance
   nextRoomFreeEntrances = freeExits(roomList[nextRoomKey].exits, True)
   selectedExit = None
   selectedEntrance = None
   for exitChar in myFreeExits:
      for entranceChar in nextRoomFreeEntrances:
         if exitChar == oppositeDirection(entranceChar):
            selectedExit = exitChar
            selectedEntrance = entranceChar
   
   #check if room is valid after checks
   if selectedEntrance is None or selectedExit is None:
      # print("Failure: selectedExit or entrance still None")
      pass
   
   room.exits[selectedExit] = roomList[nextRoomKey]
   roomList[nextRoomKey].exits[selectedEntrance] = room

#pathfinding function
def findLongestPath(room, prevDirection, path):
   if prevDirection is False:
      #first function call, first room
      path.append(room)
      room.beenVisited = True
      for direction, nextRoom in room.exits.items():
         if direction != prevDirection and not nextRoom.beenVisited:
            return findLongestPath(nextRoom, direction, path)
      
   elif len(room.exits) == 1:
      #deadend
      path.append(room)
      room.beenVisited = True
      return path
   else:
      currentDistance = len(path)
      path.append(room)
      room.beenVisited = True
      for direction, nextRoom in room.exits.items():
         if direction != prevDirection and not nextRoom.beenVisited:
            newPath = findLongestPath(nextRoom, direction, path)
            if len(newPath) > currentDistance:
               path = newPath
      return path
   return path

def oppositeDirection(direction):
   if direction == "n": return "s"
   elif direction == "e": return "w"
   elif direction == "s": return "n"
   elif direction == "w": return "e"
   else: print("FAILURE: OPPOSITEDIRECTION")

#build rooms
roomList = {}
index = 0
for description in roomDescriptions:
   roomList[index] = Room(description, index)
   index += 1

#generate a random game map
for key, room in roomList.items():
   addExit(room, roomList)

print("generated first map pass")
#make sure all rooms are connected
longestPath = []
while len(longestPath) < 23:
   # newRoomKey = random.randint(0,numRegularRooms - 1)
   # addExit(roomList[newRoomKey],newRoomKey,roomList)
   for key, room in roomList.items():
      addExit(room, roomList)
   for key,room in roomList.items():
      newPath = findLongestPath(room, False, [])
      if len(newPath) > len(longestPath): longestPath = newPath
      for key, room in roomList.items():
         room.beenVisited = False

#check path
# for room in longestPath:
#    print(room.description)
#    print("")

#insert monster room near start of path
availableExits = 0
index = 0
exitsList = None
while availableExits == 0:
   exitsList = freeExits(longestPath[index].exits)
   availableExits = len(exitsList)
   if availableExits == 0: index += 1
if exitsList == None: print("FAIL")
else:
   selectedExit = random.randint(0, len(exitsList) - 1)
   selectedExit = exitsList[selectedExit]
   roomList["monster"] = Room(monsterStartRoom, "monster")
   longestPath[index].exits[selectedExit] = roomList["monster"]
   roomList["monster"].exits[oppositeDirection(selectedExit)] = longestPath[index]
   longestPath.insert(index, roomList["monster"])

#insert exit room near end of path
availableExits = 0
index = len(roomList) - 2
exitsList = None

while availableExits == 0:
   exitsList = freeExits(longestPath[index].exits)
   availableExits = len(exitsList)
   if availableExits == 0: index -= 1
if exitsList == None: print("FAIL")
else:
   selectedExit = random.randint(0, len(exitsList) - 1)
   selectedExit = exitsList[selectedExit]
   roomList["exit"] = Room(exitDescription, "exit")
   longestPath[index].exits[selectedExit] = roomList["exit"]
   roomList["exit"].exits[oppositeDirection(selectedExit)] = longestPath[index]
   longestPath.insert(index, roomList["exit"])

#insert start room in middle of path
availableExits = 0
index = math.floor(len(roomList) / 2)
exitsList = None
while availableExits == 0:
   exitsList = freeExits(longestPath[index].exits)
   availableExits = len(exitsList)
   if availableExits == 0: index -= 1
if exitsList == None: print("FAIL")
else:
   selectedExit = random.randint(0, len(exitsList) - 1)
   selectedExit = exitsList[selectedExit]
   roomList["start"] = Room(startingDescription, "start")
   longestPath[index].exits[selectedExit] = roomList["start"]
   roomList["start"].exits[oppositeDirection(selectedExit)] = longestPath[index]
   longestPath.insert(index, roomList["start"])


#create player and monster
player = Player(roomList["start"])
#select monster
monsterIndex = random.randint(0, len(monsters) - 1)
monsterKeys = list(monsters)
monsterName = monsterKeys[monsterIndex]
monsterDescription = monsters[monsterName]
monster = Monster(player, roomList["monster"], monsterName, monsterDescription)

# shortestPath = []
# findShortestPath()

#game loop start


#game loop end
#reset room tracking for monster pathfinding
for key, room in roomList.items():
   room.beenVisited = False

def generateRoomString(room):
   exits = room.exits
   # 00 10 20
   # 01 11 21
   # 02 12 22
   roomMap = [[0 for x in range(3)] for y in range(3)] 
   
   roomMap[0][0] = "X"
   roomMap[0][2] = "X"
   roomMap[2][2] = "X"
   roomMap[2][0] = "X"
   roomMap[1][1] = "o"
   roomMap[0][1] = " "

   roomMap[0][1] = " " if "w" in exits else "X"
   roomMap[1][0] = " " if "n" in exits else "X"
   roomMap[2][1] = " " if "e" in exits else "X"
   roomMap[1][2] = " " if "s" in exits else "X"

   newMap = (f"{roomMap[0][0]}{roomMap[1][0]}{roomMap[2][0]}\n" \
           f"{roomMap[0][1]}{roomMap[1][1]}{roomMap[2][1]}\n" \
           f"{roomMap[0][2]}{roomMap[1][2]}{roomMap[2][2]}")
   
   print(newMap)
   return newMap

def addRoomMap(roomMap, allMaps, curMapIndex, dirToPrevRoom):
   #roomMap = 00 01 02
   #          10 11 12
   #          20 21 22
   # col = [00, 01, 02]
   # row = [00, 10, 21]
   col = allMaps[curMapIndex[0]] #x index

   if dirToPrevR[]oom is "n":
      #insert one place above current index
      index = curMapIndex[0] - 1 if curMapIndex[0] - 1 >= 0 else 0
      
      row = [column[curMapIndex[1]] for column in allMaps]
      row.insert(index, roomMap)
      allMaps[]



def findConnection(lastRoom, thisRoom):
   for direction, room in lastRoom.exits.items():
      if room is thisRoom:
         return oppositeDirection(direction)

   print("findConnection failed")


def mapRooms(path):
   # 00 10 20
   # 01 11 21
   # 02 12 22
   allMaps = [[0 for x in range(1)] for y in range(1)]
   curMapIndex = [0,0]
   lastRoomIndex = len(path) - 1
   for index, room in enumerate(path):
      roomMap = generateRoomString(room)
      if index is not 0:
         dirToPrevRoom = findConnection(path[index - 1], room)
         curMapIndex = addRoomMap(roomMap, mapArr, curMapIndex, dirToPrevRoom)

   print(allMaps)




# monster.findPlayer()
mapRooms(longestPath)
# for room in longestPath:
#    print(room.key)

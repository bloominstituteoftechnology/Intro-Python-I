# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name):
    self.name = name
    self.inventory = []
    self.health = 10
    # self.time = clock.getTime()
    self.currentRoom = 'laboratory'
  
  # available move directions: l, r, f, b
  def playerMove(x):
    room.getCurrentRoomMoveOptions()
    # for dir in moveOptions, 
    # # # if x == dir: room.dir_move
    # # # else "Not an available move"

  def mutateScore(e):
    if(e == True and self.health < 10):
      self.health += 1
    elif(e == False and self.health > 1):
      self.health -= 1
    else:
      self.health = 0
      self.dyingDead()
      # player loses!

  def dyingDead():
    print("You've done did died dead.")

  def itemPickup():
    # pickup message including name of item
    # addItemToInventory(item)

  def useInventoryItem(c):
    # inv = self.getInventory()
    # if c IS IN INV
    # # # # Item.useItem(c)
    # # # # # # # # removeItemFromInventory()
    # # # # "Item not in inventory"

  def addItemToInventory(ai):
    self.inventory.append(i)

  def removeItemFromInventory(ri):
    del self.inventory[ri]

  


    

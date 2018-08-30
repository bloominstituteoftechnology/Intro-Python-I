# Character parent class
#Methods: attack, die, escape, takeDamage
import random
class Character:
   def __init__(self, room, name, description, hp = 1, damage = 1, accuracy = 50):
      self.name = name
      self.description = description
      self.hp = hp
      self.damage = damage
      self.accuracy = 50
      self.location = room

   def attack(self, character):
      #run an accuracy check before causing damage
      print("%s attacks %s!", self.name, character.name)
      hit = random.randint(0,100)
      if hit > self.accuracy: 
         #Pass accuracy check
         character.takeDamage(self.damage)
      else:
         #fail accuracy check
         print("%s missed!", self.name)

   def takeDamage(self, damageAmt):
      print("%s took %d damage.", self.name, damageAmt)
      self.hp -= damageAmt
      if self.hp <= 0:
         print("%s died!", self.name)
         self.location = None


########################## Player
#Methods: useItem, dropItem, attack, takeDamage
class Player(Character):
   def __init__(self, room, name = "Saxon", description = "Me", hp = 3, damage = 1, accuracy = 50, score = 0):
      Character.__init__(self, room, name, description, hp, damage, accuracy)
      self.inventory = {}
      self.score = 0

   def viewInventory(self):
      for item in self.inventory:
         print(item)

   def pickupItem(self, commands):
      if len(commands) == 1: print("What do you want to pickup?")
      elif len(self.location.inventory) == 0: print("Nothing to pickup here")
      elif commands[1] in self.location.inventory: 
         item = commands[1]
         self.inventory[item] = self.location.inventory[item]
         print(f"you picked up the {item}")
         self.location.inventory.pop(item)

      else: print("item does not exist")
   
   def dropItem(self, item):
      #remove from inventory
      self.inventory.pop(item)
      #put in room
      self.location.inventory.append(item)
   
   def getScore(self):
      print(f"Your Score: {self.score}")

##################### Enemy
#Methods: attack, die, escape, takeDamage
import random
class Enemy:
   def __init__(self, location, name, description, hp = 1, damage = 1, accuracy = 50):
      self.name = name
      self.description = description
      self.hp = hp
      self.damage = damage
      self.accuracy = 50
   def attack(self, character):
      #run an accuracy check before causing damage
      print("%s attacks %s!", self.name, character.name)
      hit = random.randint(0,100)
      if hit > self.accuracy: 
         #Pass accuracy check
         character.takeDamage(self.damage)
      else:
         #fail accuracy check
         print("%s missed!", self.name)

   def takeDamage(self, damageAmt):
      print("%s took %d damage.", self.name, damageAmt)
      self.hp -= damageAmt
      if self.hp <= 0:
         print("%s died!", self.name)
         self.location = None

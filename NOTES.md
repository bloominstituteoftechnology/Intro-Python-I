def vowel_count(s):
  return sum(c in 'aeiou' for c in s.lower())

welcome = vowel_count('Good morning CS14!')
print(welcome)

class Dog:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __repr__(self):
    return f'{self.name} is {self.age} years old'


class Bulldog(Dog):
  def __init__(self, name, age, size):
    super().__init__(name, age)
    self.size = size

    # This will override the __repr__ method in 
  def __repr__(self):
    return f'{self.name} is {self.age} years old and is a size {self.size}'

arty = Dog('Arty', 4)
print(arty)

buster = Bulldog('Buster', 9, 2)
print(buster)
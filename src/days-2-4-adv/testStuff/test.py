class Item():
  def __init__(self, name, description):
    self.name = name
    self.description = description
  def __inter__(self):
    return iter(self)


# test = [{'name':1,'desc':2},{'name':11,'desc':22},{'name':111,'desc':222}]
test = [Item('r',23423), Item('p', 234234), Item('s', 234234)]

# print([i[k] for i in test for k in i if k=='name'])

x = []
for i in test:
  print(i)
  x.append(i.name)

print(x)


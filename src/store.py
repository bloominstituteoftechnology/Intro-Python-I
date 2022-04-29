# lets write a store class with a name and categories\
class Store:
def __init__(self, name, categories):
    self.name = name
    self.categories = categories

def __str__(self):
    self.__repr__(self)
    ret = f"{self.name}"
    for i, c enumerate(self.categories):
        ret += " " + str(i + 1)

        return ret
# how can we represent this class data as a string?

class Store:
    def __init__(self, name, categories):
        #attributes
        self.name = name
        self.categories = categories

my_store = Store("Eric's Bodega", ["drinks", "salad"])
print(my_store)
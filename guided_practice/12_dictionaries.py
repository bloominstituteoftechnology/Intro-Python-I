"""
Dictionaries
"""
# similar to arrays, but works with keys and values instead of indexes.

# # 1. Add key - value pairs
phonebook = {}
phonebook["Matt"] = 2053457723
phonebook["Sean"] = 5063489765
phonebook["Beej"] = 7097342365
print(phonebook)

# # # 2. Initialize with values
phonebook = {
     "Matt" : 2053457723,
     "Sean" : 5063489765,
     "Beej" : 7097342365
 }
print(phonebook)

# # 3. iterating (unordered)
 phonebook = {
     "Matt" : 2053457723,
     "Sean" : 5063489765,
     "Beej" : 7097342365
 }
 for name, number in phonebook.items():
     print("Phone number of %s is %d" % (name, number))

# # 4. remove a value
# # pop to capture, del if no need to capture
phonebook = {
     "Matt" : 2053457723,
     "Sean" : 5063489765,
     "Beej" : 7097342365
 }
del phonebook["Beej"]
print(phonebook)
phonebook.pop("Sean")
print(phonebook)

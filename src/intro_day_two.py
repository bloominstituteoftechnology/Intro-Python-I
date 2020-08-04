# JS objects
# swift dictionaries
# java hashmaps?

# init a empty dict
c = {}

# one primary use case is to associate 
# dicts provide very efficient fetching of keys
# dicts provide de-duplication functionality since they
# never store duplicates of any keys






#create a dict with two key-value pairs

e = {"foo":12, 11:"bar" }

#print out the value 12 from the dict

print(e["foo"])
print(e[11])

#we can also iterate through dict key pairs
for key in e:

    print(key, e[key])


#iterate through key value pairs
for key, val in e.items():
    print(key, val)
    #also interpolation
    print(f"Key is {key} and val is {val}")


#the `items` methodon dicts is similar to the  `enumerate` function for lists in that both 
# give you access to index-value/key-value
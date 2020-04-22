animals1_arr = ['snail', 'eel', 'lobster']
# animals1 = {'snail', 'eel', 'lobster'}
animals2_arr = ['snail', 'eel', 'fish']
# animals2 = {'snail', 'eel', 'fish'}

animals1 = set(animals1_arr)
animals2 = set(animals2_arr)


duplicates = animals1.intersection(animals2)
print(duplicates)

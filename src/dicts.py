# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
  {
    'lat': 'x1',
    'lon': 'y1',
    "name": 'z1',
  },
  {
    'lat': 'x2',
    'lon': 'y2',
    "name": 'z2',
  },
  {
    'lat': 'x3',
    'lon': 'y3',
    "name": 'z3',
  },
]
print(waypoints)

# Write a loop that prints out all the field values for all the waypoints
for index, dic in enumerate(waypoints):
  print('Dic: %s' % (index))
  for i in dic:
    print("""
    key: {0} - value: {1}
    """.format(i, dic[i]))



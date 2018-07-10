# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
  { "lat": 64747,
    "lon": 76474,
    "name": "somewhere"
  },
  { "lat": 5673,
    "lon": 2345,
    "name": "new waypoint"
  },
  { "lat": 8444,
    "lon": 2344,
    "name": "my waypoint"
  }
]

# Write a loop that prints out all the field values for all the waypoints
for waypoint in waypoints:
  print('Waypoint : ', waypoint['name'])
  print('latitude : ', waypoint['lat'])
  print('longitude : ', waypoint['lon'])

# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
  {
    "lat": 12.3232,
    "lon": 3.1223,
    "name": "San Francisco"
  },
   {
    "lat": 62.3232,
    "lon": 334.1223,
    "name": "Merced"
  },
   {
    "lat": 232.3232,
    "lon": 13.1223,
    "name": "New Your"
  }
]

# Write a loop that prints out all the field values for all the waypoints

for obj in waypoints:
  print(obj["lat"], obj["lon"], obj["name"])
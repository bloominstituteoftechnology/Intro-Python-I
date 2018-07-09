# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
  {
    "lat": 36.395912,
    "lon": -91.888281,
    "name": "Somewhere in USA"
  },
  {
    "lat": 36.385912,
    "lon": -91.889281,
    "name": "Somewhere else in USA"
  },
  {
    "lat": 36.395812,
    "lon": -91.898281,
    "name": "Somewhere else again in USA"
  }
]

# Write a loop that prints out all the field values for all the waypoints
for x in waypoints:
  print(x)

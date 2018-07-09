# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
  {
    "lat": 83.18912,
    "lon": -43.203281,
    "name": "Antioch, CA"
  },
  {
    "lat": 36.388322,
    "lon": -91.83281,
    "name": "Paris"
  },
  {
    "lat": 36.3932812,
    "lon": -91.843281,
    "name": "Miami, FL"
  }
]

# Write a loop that prints out all the field values for all the waypoints

for x in waypoints:
    print x
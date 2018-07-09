# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
  {
    "lat": 2108.21,
    "lon": 321.00,
    "name": "WP 1"
  },
  {
    "lat": 2103.01,
    "lon": 321.00,
    "name": "WP 2"
  },
  {
    "lat": 2000.21,
    "lon": 300.00,
    "name": "WP 3"
  }
]

# Write a loop that prints out all the field values for all the waypoints
for i in waypoints:
  print(i['lat'], i['lon'], i['name'])
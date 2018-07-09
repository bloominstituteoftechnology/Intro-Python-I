# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
  {
    "lat": 34.049968,
    "lon": -118.2393978,
    "name": 'Far Bar'
  },
  {
    "lat": 34.094600,
    "lon": -117.721755,
    "name": 'Eureka!'
  },
    {
    "lat": 34.0507809,
    "lon": -118.2519762,
    "name": 'La Cita'
  }
]

# Write a loop that prints out all the field values for all the waypoints
for waypoint in waypoints:
  for key in waypoint:
    print(waypoint[key])
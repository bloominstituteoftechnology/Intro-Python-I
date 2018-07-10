# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    { 'lat': 106.72888 },
    { 'lon': 0.69622 },
    { 'name': 'Kepulauan Riau' }
]

# Write a loop that prints out all the field values for all the waypoints
for dict in waypoints:
    print(dict)
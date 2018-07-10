# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {'lat': 12341234, 'lon': 132412341234, 'name': 'EXCALIBUR!'},
    {'lat': 42341234, 'lon': 543412341234, 'name': 'Prince Arthur!'},
    {'lat': 42347564, 'lon': 543412345543, 'name': 'FOR THE KING!'},
]

# Write a loop that prints out all the field values for all the waypoints

for i in waypoints:
    print(i['name'])
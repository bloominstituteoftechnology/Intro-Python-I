# Make a list of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {"lat": 234, "lon": 321, "name": "name 1"},
    {"lat": 24,"lon": 361,"name": "name 2"},
    {"lat": 699,"lon": 821,"name": "name 3"}
]

# Write a loop that prints out all the field values for all the waypoints
for i in waypoints:
    print(i.values())
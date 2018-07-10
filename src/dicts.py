# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {'Lat': 'the Latitude'},
    {'Lon': 'the Longitude'},
    {'name': 'the waypoint name'}
]


for x in waypoints:
    print(x.values(), x.keys()) 

# Write a loop that prints out all the field values for all the waypoints

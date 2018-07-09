# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {'lat': 37.6979039}, 
    {'lon': -121.925388}, 
    {'name': 'Lambda School Office'}
]

# Write a loop that prints out all the field values for all the waypoints

for x in waypoints:
    for y in x: 
        print(x[y])

    
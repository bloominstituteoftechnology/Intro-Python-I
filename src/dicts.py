# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {'lat': 40.712775, 'lon': -74.005973, 'name': 'NYC'},
    {'lat': 48.856614, 'lon': 2.352222, 'name': 'Paris'},
    {'lat': 34.052234, 'lon': -118.243685, 'name': 'Los Angeles'}
]

# Write a loop that prints out all the field values for all the waypoints
for location in waypoints:
    print(location['lat'], location['lon'], location['name'])
# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {'lat': 41.8863, 'lon': -87.6174, 'name': 'Chicago'},
    {'lat': 37.7959, 'lon': -122.4043, 'name': 'San Francisco'},
    {'lat': 48.8583, 'lon': 2.3202, 'name': 'Paris'}
]

# Write a loop that prints out all the field values for all the waypoints
for i in waypoints:
    print(i['lat'], i['lon'], i['name'])
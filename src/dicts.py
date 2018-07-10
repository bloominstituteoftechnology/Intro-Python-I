# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {'lat': 37.166820,
     'lon': -122.209596,
     'name': 'Big Basin Redwoods State Park'},

    {'lat': 39.236552,
     'lon': -119.985797,
     'name': 'Lake Tahoe'},

    {'lat': 36.578285,
     'lon': -118.740423,
     'name': 'General Sherman Tree'},

    {'lat': 37.743551,
     'lon': -119.523082,
     'name': 'half dome'},
]

# Write a loop that prints out all the field values for all the waypoints
for i in waypoints:
    print(i['lat'], i['lon'], i['name'])
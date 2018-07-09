# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        'lat': 100,
        'lon': 200,
        'name': 'Teh Frawg!'
    },
    {
        'lat': 200,
        'lon': 100,
        'name': 'Teh Bawse!'
    }
]

# Write a loop that prints out all the field values for all the waypoints
for i in waypoints:
    print('-------------------')
    for j in i:
        print(j, ':', i[j])

# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        'lat': '27.979168',
        'lon': '-82.539337',
        'name': 'TPA'
    },
    {
        'lat': '36.131687',
        'lon': '-86.668823',
        'name': 'BNA'
    },
    {
        'lat': '39.849312',
        'lon': '-104.673828',
        'name': 'DEN'
    }
]

# Write a loop that prints out all the field values for all the waypoints
for entry in waypoints:
    print(entry)

for entry in waypoints:
    print('{e[name]} is located at {e[lat]} latitude, {e[lon]} longitude.'.format(e=entry))

# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        "lat": 48.858370,
        "lon": 2.294481,
        "name": "Eiffel Tower"
    },
    {
        "lat": 13.412469,
        "lon": 103.866986,
        "name": "Angkor Wat"
    },
    {
        "lat": 36.106965,
        "lon": -112.112997,
        "name": "Grand Canyon"
    },
]

# Write a loop that prints out all the field values for all the waypoints

for i in waypoints:
    print(i)
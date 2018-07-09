# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        "lat": 33,
        "long": 33,
        "waypoint_name": "waypoint_one"
    },
    {
        "lat": 32,
        "long": 32,
        "waypoint_name": "waypoint_two"
    },
    {
        "lat": 31,
        "long": 31,
        "waypoint_name": "waypoint_three"
    }
]

# print(waypoints)

# Write a loop that prints out all the field values for all the waypoints

for name in waypoints:
    print("The name of the waypoint is {0[waypoint_name]}.".format(name))
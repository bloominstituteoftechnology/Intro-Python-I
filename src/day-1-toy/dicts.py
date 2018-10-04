# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Write a loop that prints out all the field values for all the waypoints
# def print_values(a):
#     """prints all the values of a dict in a list"""
#     for x in a:
#         for y in x:
#             print(x[y])

def print_values(a):
    """ prints key value pairs for all dicts"""
    for x in a:
        for y in x:
            print(f'{y}: {x[y]}')

print_values(waypoints)

# Add a new waypoint to the list
waypoints.append({"lat": 12, "long": -112, "name": "my place"})

print_values(waypoints)

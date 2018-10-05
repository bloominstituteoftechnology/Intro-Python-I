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
# for x in waypoints:
#     print(x.values())
#ONE WAY

def loopfunc(list):
    for i in list:
        for key in i:
            print(key, ': ', i[key])

loopfunc(waypoints)
#ANOTHER WAY

# Add a new waypoint to the list
waypoints.append({"lat":422, "lon": -5454, "name":"a fourth place"})
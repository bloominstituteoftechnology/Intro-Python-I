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
    },
    {
        "lat": 55,
        "lon": -65,
        "name": "made up place"
    },
    {
        "lat": 32,
        "lon": 50,
        "name": "not real place"
    },
    {
        "lat": 99,
        "lon": 44,
        "name": "a really fake place"
    }
]

# Write a loop that prints out all the field values for all the waypoints
# for i in waypoints:
#     for x in i:
#         print(i[x])
# Add a new waypoint to the list
extraWaypoint = {
    "lat": 22,
    "lon": -100,
    "name": "awesome spot"
}

waypoints.append(extraWaypoint)
for place in waypoints:
    for x in place:
        print(x, ':', place[x])
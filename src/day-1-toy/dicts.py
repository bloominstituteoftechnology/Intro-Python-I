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
for v in waypoints:
    # print(v)
    # print('The name of the waypoint is {0[name]}.'.format(v))
    # print(v['name'], v['lat'], v['lon'])
    # values = v.values()
    print(v.values())

# for w in waypoints:
#     print ('lat: %d, lon: %d, name: %s' % w['lat'], w['lon'], w['name'])

# Add a new waypoint to the list
# ?
waypoints.append({"lat": 544, "lon": 76, "name": "Forth"})


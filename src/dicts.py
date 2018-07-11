# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [{
    "lat": 90,
    "log": 15,
    "name": "home"
},
{
    "lat": 90,
    "log": 85,
    "name": "store"
},
{
    "lat": 30,
    "log": 20,
    "name": "bridge"
}]

w = [ 90, 15, "home" ]

# Write a loop that prints out all the field values for all the waypoints

for name in waypoints:
    print("The name of the waypoint is {0[name]}.".format(name))

for i in w:
    print(i)
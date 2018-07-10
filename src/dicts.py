# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [{
    'lat': 1,
    'lon': 1.5,
    'name': 'closest'
},
{
    'lat': 2,
    'lon': 2.5,
    'name': 'close'
},{
    'lat':3,
    'lon':3.5,
    'name': 'not so close'
}
]

# Write a loop that prints out all the field values for all the waypoints
for i in waypoints:
    print(i['lat'], i['lon'], i['name'])

for name in waypoints:
    print("The name of the waypoint is {0[name]}.".format(name))
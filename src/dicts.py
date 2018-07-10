# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

## Lets go to Brazil!!
waypoints = [
{"lat": 14.23},
{"lon": 51.23},
{"name": "Brazil"}
]

# Write a loop that prints out all the field values for all the waypoints
for x in waypoints:
    print(x.values(), x.keys())

## runing my code in repl.it at the moment
## dict_values([14.23]) dict_keys(['lat'])
## dict_values([51.23]) dict_keys(['lon'])
## dict_values(['Brazil']) dict_keys(['name'])
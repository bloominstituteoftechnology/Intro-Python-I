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
# QQQQQQQQ:Are we supposed to print both the keys and values and not just the values?

for i in waypoints:
    print(i)

#nested for loop for (x,y) in items: print y



# Add a new waypoint to the list

waypoints.append({
    "lat": 80,
    "lon": -160,
    "name": "bleep bloop place"
})

for i in waypoints:
    print(i)

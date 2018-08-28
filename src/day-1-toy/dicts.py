# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

## Lets go to Brazil!!
waypoints = [
    {
        "lat": 14.23,
        "lon": 51.23,
        "name": "Brazil"
    },
    {
        "lat": 11.34,
        "lon": 51.55,
        "name": "Panama"
    },
    {
        "lat": 10.34,
        "lon": 40.32,
        "name": "SF - Lambda HQ"
    }
]

# Write a loop that prints out all the field values for all the waypoints
for i in waypoints:
    for x, y in i.items():
        print(y)



# Add a new waypoint to the list

waypoints.append({
   “lat”: 10,
   “lon”: 322,
   “name”: “San Diego”
})
                  


# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        "lat": -30,
        "lon": 125,
        "name": "Middle of the outback"
    },
    {
        "lat": 41,
        "lon": -100,
        "name": "somwhere between Lexington and North Platte, Nebraska"
    },
    {
        "lat": 60,
        "lon": 90,
        "name": "Yenisey River, in Russia"
    }
]

# Write a loop that prints out all the field values for all the waypoints
def loopfunc(list):
    for i in list:
        for key in i:
            print(key, ': ', i[key])

# Add a new waypoint to the list

waypoints.append({
    "lat": -39,
    "lon": -62,
    "name": "Punta Alta, Argentina"
})

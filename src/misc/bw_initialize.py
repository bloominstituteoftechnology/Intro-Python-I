@csrf_exempt
@api_view(["GET"])
def initialize(request):
    global rooms
    user = request.user
    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = player.room()
    sewer_rooms = Room.objects.filter(sewer=room.sewer)
    sewer_map = {
        "sewer": room.sewer,
        "rooms": [{
            'id': i.id,
            'x': i.x,
            'y': i.y,
            'n_to': i.n_to,
            's_to': i.s_to,
            'e_to': i.e_to,
            'w_to': i.w_to,
        } for i in sewer_rooms]
    }
    rooms_visited = PlayerVisited.objects.filter(player=player)
    visited_list = [i.room.id for i in rooms_visited]
    players = room.playerNames(player_id)

    return JsonResponse({'uuid': uuid, 'name': player.user.username, 'inventory': player.items(), 'room_id': room.id, 'title': room.title, 'description': room.description, 'room_items': room.items(), 'sewer_map': sewer_map, 'visited': visited_list, 'players': players}, safe=True)

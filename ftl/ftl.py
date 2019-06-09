
import imagesearch, math
from interactions import image_find
from mechanics import compass_bearing


def jump_routes():
    future_waypoints = imagesearch.imagesearch_list("./ftl/img/ftl-WAYPOINT.png", .8)
    visited_waypoints = imagesearch.imagesearch_list("./ftl/img/ftl-WAYPOINT-VISITED.png",.8)
    # jump_routes = imagesearch.imagesearch_list("./ftl/img/ftl-JUMP-ROUTE.png",.9)
    possible_waypoints = []
    route_bearings = []
    current_waypoint = tuple(visited_waypoints[-1])

    #get waypoints with bearing and distance
    for waypoint in future_waypoints:
        waypoint_info = []
        bearing = int(compass_bearing(current_waypoint, tuple(waypoint)))
        distance = int(math.hypot(current_waypoint[0] - waypoint[0], current_waypoint[1] - waypoint[1]))
        waypoint_info.append(waypoint)
        waypoint_info.append(bearing)
        waypoint_info.append(distance)
        possible_waypoints.append(waypoint_info)

    print('visited waypoints:')
    for i in visited_waypoints:
        print(i)

    print('future waypoints:')
    for i in future_waypoints:
        print(i)

    #match route bearings to waypoint bearings


def start_game():
    # select ftl

    #select newgame
    image_find("./ftl/img/ftl-NEWGAME.png")

    #confirm newgame
    image_find("./ftl/img/ftl-CONFIRM.png")

    #Start newgame
    image_find("./ftl/img/ftl-START.png")

    #Continue New Game
    image_find("./ftl/img/ftl-CONTINUE.png")

    #Jump!
    image_find("./ftl/img/ftl-JUMP.png")

    image_find("./ftl/img/ftl-WAYPOINT.png")



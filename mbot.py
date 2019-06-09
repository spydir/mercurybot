# https://pyautogui.readthedocs.io/en/latest/introduction.html

from pyautogui import press, moveTo, click, size

import imagesearch, time, random, decimal, math
from PIL import Image


def keyboard(key):
    press(key)

    # moveTo(x,y,duration=num_seconds)
    # click(button=button)
    # click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')


def image_find(image):
    im = Image.open(image)
    width, height = im.size
    pause = decimal.Decimal(random.randrange(30,70))/100
    print(pause)

    timeout = time.time() + 17  # 17 seconds from now
    while True:
        pos = imagesearch.imagesearch_loop(image,.5)
        x = ((pos[0]/2)+(width/4))
        y = ((pos[1]/2)+(height/4))
        test = 0
        if test == 5 or time.time() > timeout:
            break
        test = test - 1

        if pos[0] != -1:
            print("position : ", x, y)
            moveTo(x, y, duration=.2)
            time.sleep(pause)
            click(x, y)
            break
        else:
            print("image not found")


def determine_game_state():
    #not running
    #running but not in focus
    #running - main menu
    #running - in game
    #running - in Jump Screen
    #running - in combat
    #running - in store

    pass


def count_resources():
    # this is a turn-based game so there is lots of time to count resources between actions.
    # we will definitely want to improve this later.
    pass


def count_turns():
    pass


def game_metrics():
    # this could probably be handled with logging.
    # number of actions taken
    # number of resources taken
    # amount of damage dealt
    # amount of damage received
    # number of enemies fought, defeated, they fled, we fled
    # number of stores visited
    # amount of credits received
    # amount of credits spent
    pass


def compass_bearing(pointA, pointB):
    """
    Calculates the bearing between two points.

    The formulae used is the following:
        θ = atan2(sin(Δlong).cos(lat2),
                  cos(lat1).sin(lat2) − sin(lat1).cos(lat2).cos(Δlong))

    :Parameters:
      - `pointA: The tuple representing the latitude/longitude for the
        first point. Latitude and longitude must be in decimal degrees
      - `pointB: The tuple representing the latitude/longitude for the
        second point. Latitude and longitude must be in decimal degrees

    :Returns:
      The bearing in degrees

    :Returns Type:
      float
    """
    if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError("Only tuples are supported as arguments")

    lat1 = math.radians(pointA[0])
    lat2 = math.radians(pointB[0])

    diffLong = math.radians(pointB[1] - pointA[1])

    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
            * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.atan2(x, y)

    # Now we have the initial bearing but math.atan2 return values
    # from -180° to + 180° which is not what we want for a compass bearing
    # The solution is to normalize the initial bearing as shown below
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing


def jump_routes():
    future_waypoints = imagesearch.imagesearch_list("./FTL/FTL-WAYPOINT.png", .8)
    visited_waypoints = imagesearch.imagesearch_list("./FTL/FTL-WAYPOINT-VISITED.png",.8)
    jump_routes = imagesearch.imagesearch_list("./FTL/FTL-JUMP-ROUTE.png",.9)
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


    #get routes and rout bearings
    for i in jump_routes:
        print(i)

    for i in visited_waypoints:
        print(i)
    # unique_routes = [list(x) for x in set(tuple(x) for x in jump_routes)]
    #
    #
    # for route in unique_routes:
    #     print(current_waypoint, route)
    #     route_bearings.append(int(compass_bearing(current_waypoint, tuple(route))))

    # for i in sorted(set(route_bearings)):
    #     print(i)
    #match route bearings to waypoint bearings


def ftl():
    # imageFind("./FTL/006-JUMP.png")
    moveTo(1360/2,1800/2,duration=.2)
    #start steam

    image_find("./FTL/STEAM-ICON.png")

    #select library
    image_find("./FTL/STEAM-LIBRARY.png")

    #select FTL
    image_find("./FTL/STEAM-FTL-GAME.png")

    #press play
    image_find("./FTL/STEAM-PLAY.png")

    #select newgame
    image_find("./FTL/FTL-NEWGAME.png")

    #confirm newgame
    image_find("./FTL/FTL-CONFIRM.png")

    #Start newgame
    image_find("./FTL/FTL-START.png")

    #Continue New Game
    image_find("./FTL/FTL-CONTINUE.png")

    #Jump!
    image_find("./FTL/FTL-JUMP.png")

    image_find("./FTL/FTL-WAYPOINT.png")

    #Start newgame
    image_find("./FTL/FUEL16.png")







jump_routes()




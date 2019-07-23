
import math


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


def determine_game_state():
    #not running
    #running but not in focus
    #running - main menu
    #running - in game
    #running - in Jump Screen
    #running - in combat
    #running - in store

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

def compass_distance(pointA,pointB):
    dist = math.hypot(pointB[0] - pointA[0], pointB[1] - pointA[1])
    return  dist
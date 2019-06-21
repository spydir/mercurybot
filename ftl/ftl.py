
import imagesearch, math, time, decimal, random, datetime, os, logging
from steam import steam
from interactions import image_find
from pyautogui import click,moveTo,press
from mechanics import compass_bearing
from ftl import combat


def get_waypoints():
    logging.debug("Collecting Jump Routes.")
    time.sleep(.5)
    future_waypoints = imagesearch.imagesearch_list("./ftl/img/map/unexplored_waypoint.png", .9)
    visited_waypoints = imagesearch.imagesearch_list("./ftl/img/map/explored_waypoint.png",.9)
    possible_waypoints = []
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

    return visited_waypoints, future_waypoints, possible_waypoints

    #match route bearings to waypoint bearings


def navigate_waypoints(waypoints):
    if imagesearch.imagesearch("./ftl/img/map/unexplored_waypoint.png"):
        for waypoint in waypoints:

            moveTo(waypoint[0] / 2, waypoint[1] / 2, .2)
            click(waypoint[0] / 2, waypoint[1] / 2, 1, .1, 'left')
            logging.info("{} Waypoint Clicked ".format(waypoint))
            # need time between clicking on waypoints
            # time.sleep(decimal.Decimal(random.randrange(15, 20)) / 100)

            if imagesearch.imagesearch("./ftl/img/HUD/ftl-JUMP.png") == True:
                logging.info("{} Successful Jump! ".format(waypoint))
                # need time for the target screen to pop up.
                # time.sleep(decimal.Decimal(random.randrange(135, 155)) / 100)
                return waypoint, True

            logging.info("{} Failed Jump. ".format(waypoint))
            if waypoint == waypoints[-1]:
                return waypoint, False


def handle_encounter(waypoint):
    encounter_type = ""

    logging.info("{} Assessing encounter.".format(waypoint))
    if imagesearch.imagesearch("./ftl/img/HUD/target.png"):

        logging.info("{} Ship Encountered.".format(waypoint))
        # capture region 526x418
        # save('ship_encounters',imagesearch.region_grabber([526, 418,1730,1172]))
        encounter_type = "SHIP"
        return encounter_type


    if imagesearch.imagesearch("./ftl/img/HUD/target.png") == False:

        logging.info("{} No Ship Encountered.".format(waypoint))
        # capture region 825x418
        # save('no_ship_encounters',imagesearch.region_grabber([825, 418,2030,1172]))
        # combat.non_ship_encouter()
        encounter_type = "NOSHIP"
        return encounter_type


def new_game():
    #log instance id
    gameid = "ftl:" + str(datetime.datetime.now())
    logging.info("Game Start: {}".format(gameid))
    logging.info("Starting New Game.")
    # check for loading screen, when loading screen stops go to new game button.
    # select newgame
    time.sleep(5)
    image_find("./ftl/img/new_game/ftl-NEWGAME.png", clicky=True, wait=5)

    # confirm newgame
    image_find("./ftl/img/new_game/ftl-NEWGAME-CONFIRM.png",clicky=True)

    # Start newgame
    image_find("./ftl/img/new_game/ftl-NEWGAME-START.png",clicky=True)

    # Continue New Game
    image_find("./ftl/img/DIALOG/continue.png",clicky=True)


def play_game():
    logging.info("Playing Game.")
    image_find("./ftl/img/HUD/ftl-JUMP.png",clicky=True)

    visited, future, possible = get_waypoints()

    waypoint, jump = navigate_waypoints(future)

    if jump:
        encounter = handle_encounter(waypoint)
        if encounter == "SHIP":
            combat.ship_encouter()
            combat.fight()
            # restart_game()

        if encounter != "SHIP":
            restart_game()

    else:
        logging.info("Jump Error!")
        # restart_game()


def exit_game():
    logging.info("Clicking Exit.")
    moveTo(186/2,102/2,.3)
    time.sleep(.3)
    click(186/2,102/2,1,.2)
    logging.info("Exiting Game.")


def restart_game():
    logging.info("Restarting Game.")
    press("escape")
    image_find("./ftl/img/new_game/restart.png", clicky=True)
    image_find("./ftl/img/new_game/restart_yes.png", clicky=True)
    image_find("./ftl/img/DIALOG/continue.png", clicky=True)
    play_game()


def save(index, image): # here index is the class of the image eg 2,3 etc
    mypath = str("images/" + index)
    files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    file_id = files.__len__()
    filename = mypath + "/" + str(file_id + 1) + ".png"
    logging.debug("Saving Screenshot: {}".format(filename))
    image.save(filename)
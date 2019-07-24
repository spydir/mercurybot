
import time, datetime, os, logging, pyautogui, hashlib
from utils import imagesearch, mechanics
from utils.interactions import image_find
# from pyautogui import click,moveTo,press
from utils.mechanics import compass_bearing
from ftl import combat


def get_waypoints():
    logging.debug("ftl.get_waypoints: function entered")
    time.sleep(.5)
    future_waypoints = imagesearch.imagesearch_list("./ftl/img/map/unexplored_waypoint.png", .9)
    visited_waypoints = imagesearch.imagesearch_list("./ftl/img/map/explored_waypoint.png", .9)
    possible_waypoints = []
    current_waypoint = tuple(visited_waypoints[-1])

    # #get waypoints with bearing and distance
    # for waypoint in future_waypoints:
    #     waypoint_info = []
    #     bearing = int(compass_bearing(current_waypoint, tuple(waypoint)))
    #     distance = int(math.hypot(current_waypoint[0] - waypoint[0], current_waypoint[1] - waypoint[1]))
    #     waypoint_info.append(waypoint)
    #     waypoint_info.append(bearing)
    #     waypoint_info.append(distance)
    #     possible_waypoints.append(waypoint_info)

    return current_waypoint, visited_waypoints, future_waypoints, possible_waypoints

    #match route bearings to waypoint bearings


def navigate_waypoints(gameid,zone, jumps, current, waypoints):
    logging.debug("ftl.navigate_waypoints: function entered")
    if imagesearch.imagesearch("./ftl/img/map/unexplored_waypoint.png"):
        for waypoint in waypoints:
            dist = mechanics.compass_distance(tuple(current), tuple(waypoint))
            bearing = mechanics.compass_bearing(tuple(current), tuple(waypoint))

            pyautogui.moveTo(waypoint[0] / 2, waypoint[1] / 2, .2)
            pyautogui.click(waypoint[0] / 2, waypoint[1] / 2, 1, .1, 'left')
            logging.debug("{} ftl.navigate_waypoints: waypoint clicked ".format(waypoint))
            # need time between clicking on waypoints
            # time.sleep(decimal.Decimal(random.randrange(15, 20)) / 100)

            if imagesearch.imagesearch("./ftl/img/HUD/ftl-JUMP.png") == True:

                logging.info("{} ftl.navigate_waypoints: successful jump!".format([gameid, zone, jumps, current, tuple(waypoint), dist, bearing, True]))
                # need time for the target screen to pop up.
                # time.sleep(decimal.Decimal(random.randrange(135, 155)) / 100)
                return waypoint, True

            logging.info("{} ftl.navigate_waypoints: failed jump!".format([gameid, zone, jumps, current, tuple(waypoint), dist, bearing, False]))
            if waypoint == waypoints[-1]:
                return waypoint, False


def handle_encounter(waypoint="0,0"):
    logging.debug("ftl.handle_encounter: function entered")
    encounter_type = ""

    logging.debug("{} Assessing encounter.".format(waypoint))
    time.sleep(3)
    target = imagesearch.imagesearch("./ftl/img/HUD/hostile_target.png",.7)
    print(target)
    if target:
        log_entry = [datetime.datetime,waypoint]
        logging.debug("{} Ship Encountered.".format(log_entry))
        # capture region 526x418
        # save('ship_encounters',imagesearch.region_grabber([526, 418,1730,1172]))
        encounter_type = "SHIP"
        return encounter_type

    if imagesearch.imagesearch("./ftl/img/HUD/hostile_target.png",.7):
        log_entry = [datetime.datetime, waypoint]
        logging.debug("{} Ship Encountered.".format(log_entry))
        # capture region 526x418
        # save('ship_encounters',imagesearch.region_grabber([526, 418,1730,1172]))
        encounter_type = "SHIP"
        return encounter_type

    else:
        log_entry = [datetime.datetime, waypoint]
        logging.debug("{} No Ship Encountered.".format(log_entry))
        # capture region 825x418
        # save('no_ship_encounters',imagesearch.region_grabber([825, 418,2030,1172]))
        encounter_type = "NOSHIP"
        return encounter_type


def new_game():
    gameid_str = "ftl:" + str(datetime.datetime.now())
    hash_object = hashlib.md5(gameid_str.encode())
    gameid = hash_object.hexdigest()
    logging.debug("ftl.new_game:".format(gameid))

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

    return gameid


def play_game(gameid):
    logging.debug("ftl.play_game: function entered")
    zone = 1
    jumps = 0
    image_find("./ftl/img/HUD/ftl-JUMP.png",clicky=True)

    current, visited, future, possible = get_waypoints()

    waypoint, jump = navigate_waypoints(gameid,zone,jumps,current,future)

    if jump:
        jumps += 1
        encounter = handle_encounter(waypoint)
        if encounter == "SHIP":
            logging.debug("ftl.play_game: entered ship encounter")
            # combat.ship_encounter()
            # combat.fight()
            restart_game()

        if encounter != "SHIP":
            logging.debug("ftl.play_game: entered non-ship encounter")
            restart_game()


    else:
        logging.debug("Jump Error!")
        pyautogui.press('escape')
        restart_game()


def exit_game():
    logging.debug("ftl.exit_game: function entered")
    pyautogui.moveTo(186/2,102/2,.3)
    time.sleep(.3)
    pyautogui.click(186/2,102/2,1,.2)


def restart_game():
    gameid_str = "ftl:" + str(datetime.datetime.now())
    hash_object = hashlib.md5(gameid_str.encode())
    gameid = hash_object.hexdigest()
    logging.debug("ftl.restart:".format(gameid))

    time.sleep(3)
    pyautogui.press("escape")

    image_find("./ftl/img/new_game/restart.png", clicky=True)
    image_find("./ftl/img/new_game/restart_yes.png", clicky=True)
    image_find("./ftl/img/DIALOG/continue.png", clicky=True)
    play_game(gameid)


def save_screenshot(index, image): # here index is the class of the image eg 2,3 etc
    logging.debug("ftl.save_screenshot: function entered")
    mypath = str("images/" + index)
    files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    file_id = files.__len__()
    filename = mypath + "/" + str(file_id + 1) + ".png"
    logging.debug("Saving Screenshot: {}".format(filename))
    image.save(filename)
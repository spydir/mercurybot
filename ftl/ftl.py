
import imagesearch, math, time, decimal, random, datetime, os, logging
from steam import steam
from interactions import image_find
from pyautogui import click,moveTo
from mechanics import compass_bearing





def jump_routes():
    future_waypoints = imagesearch.imagesearch_list("./ftl/img/ftl-WAYPOINT.png", .9)
    visited_waypoints = imagesearch.imagesearch_list("./ftl/img/ftl-WAYPOINT-VISITED.png",.9)
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


def start_game():
    # select ftl

    # select newgame
    image_find("./ftl/img/ftl-NEWGAME.png", clicky=True)

    # confirm newgame
    image_find("./ftl/img/ftl-CONFIRM.png",clicky=True)

    # Start newgame
    image_find("./ftl/img/ftl-START.png",clicky=True)

    # Continue New Game
    image_find("./ftl/img/ftl-CONTINUE.png",clicky=True)


def play_game():

    # Jump!
    image_find("./ftl/img/ftl-JUMP.png",clicky=True)

    visited, future, possible = jump_routes()

    for i in future:
        click(i[0]/2, i[1]/2, 1, .6, 'left')
        logging.info("{} Waypoint Clicked ".format(i))

        pause = decimal.Decimal(random.randrange(52, 87)) / 100
        time.sleep(pause)
        if imagesearch.imagesearch("./ftl/img/ftl-WAYPOINT.png") == False:
            logging.info("{} Successful Jump! ".format(i))

            time.sleep(decimal.Decimal(random.randrange(500, 800)) / 100)
            logging.info("{} Looking for Target.".format(i))

            if imagesearch.imagesearch("./ftl/img/ftl-TARGET.png") == True:

                logging.info("{} Ship Encountered. ".format(i))
                #capture region 526x418
                save('ship_encounters',imagesearch.region_grabber([526, 418,1730,1172]))

            time.sleep(decimal.Decimal(random.randrange(25, 39)) / 100)
            if imagesearch.imagesearch("./ftl/img/ftl-TARGET.png") == False:
                logging.info("{} No Ship Encountered. ".format(i))
                #capture region 825x418
                save('no_ship_encounters',imagesearch.region_grabber([825, 418,2030,1172]))
            restart_game()
            break
        logging.info("{} Failed Jump. ".format(i))
        if i == future[-1]:
            restart_game()
            break


    # image_find("./ftl/img/ftl-WAYPOINT.png",clicky=True)


def exit_game():
    logging.info("Clicking Exit.")
    moveTo(186/2,102/2,.3)
    time.sleep(3)
    click(186/2,102/2,1,.2)


def restart_game():
    exit_game()
    steam.start_steam()
    start_game()
    play_game()


def save(index, image): # here index is the class of the image eg 2,3 etc
    mypath = str("images/" + index)
    files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    file_id = files.__len__()
    filename = mypath + "/" + str(file_id + 1) + ".png"
    image.save(filename)
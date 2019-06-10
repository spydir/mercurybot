
from pyautogui import moveTo
from imagesearch import imagesearch
from interactions import image_find
import logging, os


def logs():
    mypath = str("logs/")
    files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    file_id = files.__len__()
    fname = mypath + "/" + str(file_id + 1) + ".log"

    logging.basicConfig(
        filename=fname,
        level=logging.INFO,
        format="%(asctime)s:%(levelname)s:%(message)s"
        )


def start_steam():
    logging.shutdown()


    logs()

    # check to see if steam is open
        # Are the game string and play buttons visible?
    if imagesearch("./ftl/img/FTL-STEAM-GAME-STRING.png") == True:
        image_find("./steam/img/STEAM-PLAY.png", clicky=True)

        # if not, is the game listing visible?
        # if not, is steam visible?
        # if not, is the steam logo visible?
        # if not, move to the OSX icon bar

    # move to pop-up bar in OSX
    moveTo(1360 / 2, 1800 / 2, duration=.2)

    # start steam
    image_find("./steam/img/STEAM-ICON.png",clicky=True)

    # select library
    image_find("./steam/img/STEAM-LIBRARY.png",clicky=True)

    # select ftl
    image_find("./ftl/img/FTL-STEAM-GAME-LISTING.png", clicky=True)

    # press play
    image_find("./steam/img/STEAM-PLAY.png",clicky=True)


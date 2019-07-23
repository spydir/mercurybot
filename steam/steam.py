
from pyautogui import moveTo
from utils.imagesearch import imagesearch
from utils.interactions import image_find
import logging





def start_steam():

    # check to see if steam is open
        # Are the game string and play buttons visible?
    if imagesearch("./ftl/img/steam/FTL-STEAM-GAME-STRING.png") == True:
        image_find("./steam/img/STEAM-PLAY.png", clicky=True, precision=.3)
        image_find("./steam/img/STEAM-PLAY.png", clicky=True, precision=.3)

        # if not, is the game listing visible?
        # if not, is steam visible?
        # if not, is the steam logo visible?
        # if not, move to the OSX icon bar

    if imagesearch("./ftl/img/steam/FTL-STEAM-GAME-STRING.png") == False:

        # move to pop-up bar in OSX
        moveTo(1360 / 2, 1800 / 2, duration=.2)

        # start steam
        logging.debug("looking for steam icon")
        image_find("./steam/img/STEAM-ICON.png", clicky=True)

        # select library
        logging.debug("looking for steam library")
        image_find("./steam/img/STEAM-LIBRARY.png", clicky=True)

        # select ftl
        logging.debug("looking for ftl in steam")
        image_find("./ftl/img/steam/FTL-STEAM-GAME-LISTING.png", clicky=True)

        # press play
        logging.debug("looking for play button")
        image_find("./steam/img/STEAM-PLAY.png", clicky=True)

from pyautogui import moveTo

import imagesearch, math
from interactions import image_find


def start_steam():
    #check to see if steam is open
    # image_find("./ftl/img/FTL-GAME-LISTING.png")

    # move to pop-up bar in OSX
    moveTo(1360 / 2, 1800 / 2, duration=.2)

    # start steam
    image_find("./steam/img/STEAM-ICON.png")

    # select library
    image_find("./steam/img/STEAM-LIBRARY.png")

    # select ftl
    image_find("./ftl/img/FTL-GAME-LISTING.png")

    # press play
    image_find("./steam/img/STEAM-PLAY.png")
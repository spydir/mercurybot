from utils.interactions import image_find
import time,datetime
from ftl import ftl
from pyautogui import click,moveTo
import os, logging
from utils import imagesearch


def ship_encounter(combat=True):
    logging.debug("combat.ship_encounter: function entered")
    dialog = True

    if combat:

        while dialog:

            logging.debug("combat.ship_encounter: dialog loop started")
            image_find("./ftl/img/DIALOG/continue.png", clicky=True, precision=.8)
            directory = "/Users/lee/github/mercurybot/ftl/img/dialog/combat"

            for file in os.listdir(directory):
                filename = os.fsdecode(file)
                if filename.endswith(".png"):
                    logging.debug("Search For: {}".format(filename))
                    if imagesearch.imagesearch(os.path.join(directory, filename)):
                        logging.debug("Found!: {}".format(filename))
                        image_find(os.path.join(directory, filename), clicky=True, precision=.8)
                        break

                else:
                    continue
            time.sleep(1)
            if not imagesearch.imagesearch("./ftl/img/HUD/dialogbox_border.png"):
                logging.debug("combat.ship_enounter: no dialog box found")
                dialog = False

    # if combat == True:
    # # combat diaglog
    #    print(image_find("./ftl/img/DIALOG/continue.png", clicky=False))
    #     image_find("./ftl/img/DIALOG/combat/intervene_to_defend_the_outpost.png", clicky=True)
    #     image_find("./ftl/img/DIALOG/combat/fight_.png", clicky=True)
    #     image_find("./ftl/img/DIALOG/ftl-DIALOG-ATTACK_AUTOMATED_SHIP.png", clicky=True)
    #     image_find("./ftl/img/DIALOG/ftl-DIALOG-TURN_AND_FIGHT.png", clicky=True)
    #     image_find("./ftl/img/DIALOG/ftl-DIALOG-TRY_TO_BE_HERO_ATTACK_PIRATE.png", clicky=True)
    #     image_find("./ftl/img/DIALOG/ftl-DIALOG-ATTACK_THE_PIRATE.png", clicky=True)
    #     image_find("./ftl/img/DIALOG/ftl-DIALOG-ATTACK_THE_SHIP.png", clicky=True)
    #     image_find("./ftl/img/DIALOG/ftl-DIALOG-ATTACK_THE_SLAVER_SCUM.png", clicky=True)
    #     image_find("./ftl/img/DIALOG/ftl-DIALOG-REJECT.png", clicky=True)
    #     image_find("./ftl/img/DIALOG/ftl-DIALOG-ACCEPT.png", clicky=True)
    #     image_find("./ftl/img/DIALOG/ftl-DIALOG-ATTEMPT_TO_DOWNLOAD_DATA.png", clicky=True)
    #     image_find("./ftl/img/DIALOG/ftl-DIALOG-LEAD_THEM_TO_DESTINATION.png", clicky=True)
    #
    #
    # if combat == False:
    #     # Non-combat dialog
    #     image_find("./ftl/img/DIALOG/ftl-DIALOG-AVOID_THE_CONFLICT.png", clicky=True)
    #     image_find("./ftl/img/DIALOG/ftl-DIALOG-AVOID_PROVOKING_SHIP.png", clicky=True)
    #     image_find("./ftl/img/DIALOG/ftl-DIALOG-IGNORE.png", clicky=True)
    #     image_find("./ftl/img/DIALOG/ftl-DIALOG-NO_NEED_FOR_SERVICE.png", clicky=True)
    #     image_find("./ftl/img/DIALOG/ftl-DIALOG-DONT_RISK_ACTIVATING.png", clicky=True)
    #     image_find("./ftl/img/DIALOG/ftl-DIALOG-DECLINE.png", clicky=True)
    #     image_find("./ftl/img/DIALOG/ftl-DIALOG-ACCEPT_BRIBE.png", clicky=True)
    #     image_find("./ftl/img/DIALOG/ftl-DIALOG-IGNORE_THE_SLAVER_SCUM.png", clicky=True)
    #
    #
    # # chance it
    # image_find("./ftl/img/DIALOG/ftl-DIALOG-REJECT.png", clicky=True)
    # image_find("./ftl/img/DIALOG/ftl-DIALOG-ACCEPT.png", clicky=True)
    # image_find("./ftl/img/DIALOG/ftl-DIALOG-ATTEMPT_TO_DOWNLOAD_DATA.png", clicky=True)
    # image_find("./ftl/img/DIALOG/ftl-DIALOG-LEAD_THEM_TO_DESTINATION.png", clicky=True)


def non_ship_encounter():
    logging.debug("combat.non_ship_encounter: function entered")
    pass


def hud_location(area):
    logging.debug("combat.hud_location: function entered")
    logging.debug("Locating: {}".format(area))
    origin = imagesearch.imagelocate('./ftl/img/HUD/hull.png')

    if area == "target_frame":
        target_frame = [origin[0] + 1743, origin[1] + 83, origin[0] + 2504, origin[1] + 1106]  # 1922, 230 : 2683, 1253
        return target_frame

    if area == "weapon_bar":
        weapon_bar = [origin[0] + 474, origin[1] + 1216, origin[0] + 1275, origin[1] + 1315]  # 653, 1363 : 1447, 1454
        return weapon_bar


    # hull_points = [origin, (origin[0] + 726, origin[1] + 64)]
    # shield = [(origin[0] - 47, origin[1] - 83),(origin[0] - 234, origin[1] - 128)]  # 223, 227 : 413, 275
    # fuel = [(origin[0] - 292, origin[1] - 81), (origin[0] - 353, origin[1] - 126)]  # 471, 228 : 532, 273
    # missle_ammo = [(origin[0] - 426, origin[1] - 81), (origin[0] - 486, origin[1] - 126)]  # 605, 228 : 665, 273
    # drone_ammo = [(origin[0] - 559, origin[1] - 81), (origin[0] - 621, origin[1] - 126)]  # 738, 228 : 800, 273
    # credits = [(origin[0] - 814, origin[1] - 3), (origin[0] - 980, origin[1] - 79)]  # 993, 150 : 1159, 211
    # jump_button = [origin[0] - 1036, origin[1] - 33, origin[0] - 1214, origin[1] - 119]  # 1215, 180 : 1393, 266
    # ship_menu = [(origin[0] - 1243, origin[1] - 33), (origin[0] - 1366, origin[1] - 119)]  # 1422, 180 : 1545, 266
    # settings = [(origin[0] - 1396, origin[1] - 33), (origin[0] - 1481, origin[1] - 119)]  # 1575, 180 : 1660, 266
    # crew = [(origin[0] - 1, origin[1] - 288), (origin[0] - 176, origin[1] - 533)]  # 180, 435 : 355, 680
    # power = [(origin[0] - 4, origin[1] - 1222), (origin[0] - 61, origin[1] - 1363)]  # 183, 1369 : 240, 1510
    #   sector_map = [(origin[0] - 660, origin[1] - 143), (origin[0] - 2163, origin[1] - 1289)]  # 839, 290 : 2342, 1436
    # sector_count = [(origin[0] - 938, origin[1] - 1210), (origin[0] - 997, origin[1] - 1259)]  # 1117, 1357 : 1176, 1406
    # sector_type = [(origin[0] - 1035, origin[1] - 1210), (origin[0] - 1570, origin[1] - 1259)] # 1214, 1357 : 1749, 1406
    # std_dialog = [(origin[0] - 649, origin[1] - 270), (origin[0] - 1854, origin[1] - 1025)]  # 828, 417 : 2033, 1172
    # ship_dialog = [(origin[0] - 344, origin[1] - 264), (origin[0] - 1553, origin[1] - 1026)]  # 523, 411 : 1732, 1173
    # # target_frame = [(origin[0]+1743, origin[1] + 83), (origin[0] + 2504, origin[1] + 1106)]  # 1922, 230 : 2683, 1253
    # store = [(origin[0] - 658, origin[1] - 159), (origin[0] - 1839, origin[1] - 1083)]  # 837, 306 : 2018, 1230

    # sector_cancel = tuple(origin[0] - 2976, (origin[1] - 1252))
    # store_close = Tuple(origin[0] - 1696, origin[1] - 1113)  # 1875, 1260
    # close_game = Tuple(origin[0] + 61, origin[1] + 45)  # 188,102
    # minimize_game = Tuple(origin[0] - 49, origin[1] + 45)  # 228, 102
    # maximize_game = Tuple(origin[0] - 89, origin[1] + 45)  # 268, 102


def wep_locations(wep):
    logging.debug("combat.wep_locations: function entered")
    logging.debug("Locating Weapon: {}".format(wep))
    area = hud_location("weapon_bar")
    if wep == "bar":
        bar = hud_location("weapon_bar")
        print(bar)
        # imagesearch.region_grabber(bar, 'bar_region.png')
        return bar

    if wep == "weapon1":
        w1 =[(area[0]) , (area[1]) , (area[2]-600) , (area[3]) ]
        imagesearch.region_grabber(w1, 'w1_region.png')
        return w1

    if wep == "weapon2":
        w2 = [(area[0]+200) , (area[1]) , (area[2]-400) , (area[3]) ]
        # imagesearch.region_grabber(w2,'w2_region.png')
        return w2

    if wep == "weapon3":
        w3 = [(area[0]+400) , (area[1]) , (area[2]-200) , (area[3]) ]
        # imagesearch.region_grabber(w3,'w3_region.png')
        return w3

    if wep == "weapon4":
        w4 = [(area[0]+600) , (area[1]) , (area[2]) , (area[3]) ]
        # imagesearch.region_grabber(w4,'w4_region.png')
        return w4

    # w2_area = [(pos[0]+270)/2, (pos[1]-50)/2]
    # w3_area = [(pos[0]+470)/2, (pos[1]-50)/2]
    # w4_area = [(pos[0]+670)/2, (pos[1]-50)/2]


def target_locations():
    logging.debug("combat.target_locations: function entered")
    logging.debug("Aquiring Target.")
    area = hud_location("target_frame")
    # imagesearch.region_grabber(area,"region.png")
    weps = imagesearch.imagesearcharea('./ftl/img/hud/weapons.png', area[0], area[1], area[2], area[3])
    shields = imagesearch.imagesearcharea('./ftl/img/hud/shields.png', area[0], area[1], area[2], area[3])
    engines = imagesearch.imagesearcharea('./ftl/img/hud/engines.png', area[0], area[1], area[2], area[3])
    # x = (enemy_weps[0]+area[0]+15)/2
    # y = (enemy_weps[1]+area[1]+15)/2
    enemy_weps = [(weps[0]+area[0]+15)/2,(weps[1]+area[1]+15)/2]
    return enemy_weps, shields, engines


def enable_autofire():
    logging.debug("combat.enable_autofire: function entered")
    while True:
        image_find("./ftl/img/hud/autofire_disabled.png", clicky=True,precision=.88)
        if imagesearch.imagesearch("./ftl/img/hud/autofire_enabled.png"):
            logging.debug("{} enable_autofire: image found".format(datetime.datetime))
            time.sleep(.25)
            break


def weapon_status(weapon):
    logging.debug("combat.weapon_status: function entered")
    logging.debug("Checking Weapon Status: {}".format(weapon))
    area = wep_locations(weapon)
    time.sleep(1)
    # print(weapon, "disabled:",x imagesearch.imagesearcharea("./ftl/img/hud/weapon_disabled.png", area[0], area[1], area[2], area[3],.9) != [-1,-1])

    if imagesearch.imagesearcharea("./ftl/img/hud/weapon_disabled.png", area[0], area[1], area[2], area[3],.9) != [-1,-1]:
        return "DISABLED"

    else:

        return "ENABLED"


def enable_weapon(weapon):
    logging.debug("combat.enable_weapon: function entered")
    logging.debug("Attempting to enable Weapon: ", weapon)
    pos = wep_locations(weapon)
    moveTo(pos[0]/2+25, pos[1]/2+25, .1)

    while True:

        moveTo(pos[0] / 2 + 25, pos[1] / 2 + 25, .1)
        click(pos[0]/2+25, pos[1]/2+25)
        time.sleep(.25)
        moveTo(pos[0] / 2 - 25, pos[1] / 2 - 25, .1)

        if weapon_status(weapon) != "DISABLED":
            logging.debug("Successfully Enabled Weapon: ", weapon)
            moveTo(pos[0] / 2 + 25, pos[1] / 2 + 25, .1)
            click(pos[0] / 2 + 25, pos[1] / 2 + 25, clicks=1)
            time.sleep(.25)
            break

        logging.debug("Failure to Enable Weapon: ", weapon)


def fight():
    logging.debug("combat.fight: function entered")

    weps,shield,engines = target_locations()

    enable_autofire()

    # power-up weapon 1
    if weapon_status("weapon1") == "DISABLED":
        enable_weapon("weapon1")
    time.sleep(.25)
    moveTo(weps[0], weps[1], .1)
    click(weps[0],weps[1])

    if weapon_status("weapon2") == "DISABLED":
        enable_weapon("weapon2")
    time.sleep(.25)
    moveTo(weps[0], weps[1], .1)
    click(weps[0], weps[1])
    time.sleep(30)
    ftl.restart_game()


    # detect when fight is won

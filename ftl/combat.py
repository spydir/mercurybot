from interactions import image_find
import logging

def ship_encouter(combat=True):

    # This exhaustive list of image names should just be switched to parse through a directory of combat, non-combat and unknown dialog answers.

    if combat == True:
    # combat diaglog
        image_find("./ftl/img/DIALOG/ftl-DIALOG-CONTINUE.png", clicky=True)
        image_find("./ftl/img/DIALOG/ftl-DIALOG-INTERVENE_TO_DEFEND_OUTPOST.png", clicky=True)
        image_find("./ftl/img/DIALOG/ftl-DIALOG-FIGHT_THE_SHIP.png", clicky=True)
        image_find("./ftl/img/DIALOG/ftl-DIALOG-ATTACK_AUTOMATED_SHIP.png", clicky=True)
        image_find("./ftl/img/DIALOG/ftl-DIALOG-TURN_AND_FIGHT.png", clicky=True)
        image_find("./ftl/img/DIALOG/ftl-DIALOG-TRY_TO_BE_HERO_ATTACK_PIRATE.png", clicky=True)
        image_find("./ftl/img/DIALOG/ftl-DIALOG-ATTACK_THE_PIRATE.png", clicky=True)
        image_find("./ftl/img/DIALOG/ftl-DIALOG-ATTACK_THE_SHIP.png", clicky=True)
        image_find("./ftl/img/DIALOG/ftl-DIALOG-ATTACK_THE_SLAVER_SCUM.png", clicky=True)


    if combat == False:
        # Non-combat dialog
        image_find("./ftl/img/DIALOG/ftl-DIALOG-AVOID_THE_CONFLICT.png", clicky=True)
        image_find("./ftl/img/DIALOG/ftl-DIALOG-AVOID_PROVOKING_SHIP.png", clicky=True)
        image_find("./ftl/img/DIALOG/ftl-DIALOG-IGNORE.png", clicky=True)
        image_find("./ftl/img/DIALOG/ftl-DIALOG-NO_NEED_FOR_SERVICE.png", clicky=True)
        image_find("./ftl/img/DIALOG/ftl-DIALOG-DONT_RISK_ACTIVATING.png", clicky=True)
        image_find("./ftl/img/DIALOG/ftl-DIALOG-DECLINE.png", clicky=True)
        image_find("./ftl/img/DIALOG/ftl-DIALOG-ACCEPT_BRIBE.png", clicky=True)
        image_find("./ftl/img/DIALOG/ftl-DIALOG-IGNORE_THE_SLAVER_SCUM.png", clicky=True)


    # chance it
    image_find("./ftl/img/DIALOG/ftl-DIALOG-REJECT.png", clicky=True)
    image_find("./ftl/img/DIALOG/ftl-DIALOG-ACCEPT.png", clicky=True)
    image_find("./ftl/img/DIALOG/ftl-DIALOG-ATTEMPT_TO_DOWNLOAD_DATA.png", clicky=True)
    image_find("./ftl/img/DIALOG/ftl-DIALOG-LEAD_THEM_TO_DESTINATION.png", clicky=True)



def non_ship_encouter():
    pass

def fight():
    pass

    '''
        
        bound by target box:
            find "target" word and build zone with top left x,y and bottom right x,y
            within that area, find location of all systems   
               - weapons
               - shields
               - engines
               - nav
               - 02 
        
            return positions of each system
        
        select weapon x, target system y
        
        
    '''


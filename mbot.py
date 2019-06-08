# https://pyautogui.readthedocs.io/en/latest/introduction.html

from pyautogui import press, moveTo, click, size

import imagesearch, time

def keyboard(key):
    press(key)

    # moveTo(x,y,duration=num_seconds)
    # click(button=button)
    # click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

def imageFind(image):

    timeout = time.time() + 30  # 15 seconds from now
    while True:
        pos = imagesearch.imagesearch(image)
        test = 0
        if test == 5 or time.time() > timeout:
            break
        test = test - 1

        if pos[0] != -1:
            print("position : ", pos[0]/2, pos[1])
            moveTo(((pos[0]/2)+30), ((pos[1]/2)+12),duration=.2)
            time.sleep(1) #need to make this random
            click((pos[0]/2)+30, (pos[1]/2)+12) #need to change this to 1/2 image size
            break
        else:
            print("image not found")


# imageFind("./FTL/006-JUMP.png")
moveTo(1360/2,1800/2,duration=.2)
#start steam

imageFind("./FTL/STEAM-ICON.png")

#select library
imageFind("./FTL/STEAM-LIBRARY.png")

#select FTL
imageFind("./FTL/STEAM-FTL-GAME.png")

#press play
imageFind("./FTL/STEAM-PLAY.png")

#select newgame
imageFind("./FTL/FTL-NEWGAME.png")

#confirm newgame
imageFind("./FTL/FTL-CONFIRM.png")

#Start newgame
imageFind("./FTL/FTL-START.png")






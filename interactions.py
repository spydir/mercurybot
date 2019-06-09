
import time, random, decimal
from imagesearch import imagesearch_loop, click_image
from pyautogui import press, moveTo, click
from PIL import Image


def keyboard(key):
    press(key)

    # moveTo(x,y,duration=num_seconds)
    # click(button=button)
    # click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')


def image_find(image,clicky=False):
    im = Image.open(image)
    width, height = im.size
    pause = decimal.Decimal(random.randrange(35,90))/100
    print(pause)

    timeout = time.time() + 17  # 17 seconds from now
    while True:
        pos = imagesearch_loop(image,.5)
        x = ((pos[0]/2)+(width/4))
        y = ((pos[1]/2)+(height/4))

        test = 0

        # timer countdown
        if test == 5 or time.time() > timeout:
            break
        test = test - 1

        if pos[0] != -1:
            print("x and y : ", x, y)

            time.sleep(pause)
            if clicky == True:
                moveTo(x, y, duration=.2)
                click(x, y)

            return True

        else:
            print("image not found")
            return False


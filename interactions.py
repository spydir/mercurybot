
import imagesearch, time, random, decimal

from pyautogui import press, moveTo, click

from PIL import Image


def keyboard(key):
    press(key)

    # moveTo(x,y,duration=num_seconds)
    # click(button=button)
    # click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')


def image_find(image):
    im = Image.open(image)
    width, height = im.size
    pause = decimal.Decimal(random.randrange(30,70))/100
    print(pause)

    timeout = time.time() + 17  # 17 seconds from now
    while True:
        pos = imagesearch.imagesearch_loop(image,.5)
        x = ((pos[0]/2)+(width/4))
        y = ((pos[1]/2)+(height/4))
        test = 0
        if test == 5 or time.time() > timeout:
            break
        test = test - 1

        if pos[0] != -1:
            print("position : ", x, y)
            moveTo(x, y, duration=.2)
            time.sleep(pause)
            click(x, y)
            break
        else:
            print("image not found")


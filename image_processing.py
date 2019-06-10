import pytesseract, os
from PIL import Image


directory = 'images/no_ship_encounters/'



for filename in os.listdir(directory):
    if filename.endswith(".png"):
        img = Image.open(directory+filename)
        new_size = tuple(2 * x for x in img.size)
        img = img.resize(new_size, Image.ANTIALIAS)
        print(pytesseract.image_to_string(img))

        continue
    else:
        continue


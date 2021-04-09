#!/usr/bin/env python3

import sys, os
from PIL import Image

def edit_image(name, path, dest):
    image = Image.open(path)
    rotated = colorImage.rotate(90)
    resized = rotated.resize((128, 128)).convert('RGB')
    resized.save(os.path.join(dest, "{}.jpeg".format(name)))

arg = sys.argv[1:]
src, dest = arg[0], arg[1]

images = [(os.path.join(src, x), x) for x in os.listdir(src)]
for path, name in images:
    try:
        edit_image(name, path, dest)
    except:
        print("Cant Convert {}".format(name))
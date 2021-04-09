#!/usr/bin/env python3
import sys, os
from PIL import Image

def edit_image(path, name):
    PATH = os.path.join(path, name)
    img = Image.open(PATH)
    img = img.convert('RGB')
    img = img.resize((600, 400))
    img.save(PATH.split('.')[0] + '.jpeg')

if __name__ == "__main__":
    arg = sys.argv[1:]
    path = arg[0]
    img_name_list = [x for x in os.listdir(path) if '.tiff' in x]
    for img in img_name_list:
        edit_image(path, img)
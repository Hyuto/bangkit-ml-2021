import os, sys, coloredlogs, logging
from PIL import Image

LEFT_X = 330
RIGHT_X = 1600
UPPER_Y = 255

def crop_images(path, name):
    img = Image.open(path)
    width, height = img.size

    if width < RIGHT_X:
        logging.error(f'{name} : Invalid image size')
        return 1
    else:
        cropped_img = img.crop((LEFT_X, UPPER_Y, RIGHT_X, height))
        cropped_img.save(path)
        logging.info(f'{name} : Success')
        return 0

if __name__ == '__main__':
    coloredlogs.install()

    path, count = sys.argv[1], 0
    images = [(os.path.join(path, x), x) for x in os.listdir(path) if 'quizz' in x.lower()]
    for path, img in images:
        count += crop_images(path, img)
    if count == 0:
        logging.info('Done!')
    else:
        logging.warning(f'Done with {count} errors')
""" generate random terrain-like 2D image

    (c) Volker Poplawski 2018
"""
from PIL import Image, ImageFilter
import random


IMPASSABLE = 0, 0, 0
PASSABLE = 255, 255, 255


def generate_map(size, kernelsize, numiterations):
    im = Image.open('./pixil-frame-0.png',mode='r',formats=None)

    # init with random data
    for x in range(0, im.width):
        print(x)
        for y in range(0, im.height):
            im.putpixel((x, y), random.choice([IMPASSABLE, PASSABLE]))

    # apply filter multiple times
    for i in range(numiterations):
        im = im.filter(ImageFilter.RankFilter(kernelsize, kernelsize**2 // 2))

    return im





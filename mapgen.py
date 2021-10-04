""" generate random terrain-like 2D image

    (c) Volker Poplawski 2018
"""
from PIL import Image, ImageFilter
import random


IMPASSABLE = 0, 0, 0
PASSABLE = 255, 255, 255
imagePath = './images/Squares.png' # choose in the interface from certian images in the path 
# import image => you can navigate your self with any image and then it would be proccesed to the right size
# or
# load image => opens the right size 2*n (ready to use)


def generate_map(size, kernelsize, numiterations):
    orIm = Image.open(imagePath,mode='r',formats=None)
    im = Image.new('RGB', (orIm.height, orIm.width), color=IMPASSABLE)


    for x in range(0, im.width):
        print('Progress is: ', x, ' -- ',im.width)
        for y in range(0, im.height):
            coordinate = x, y 
            rgba = orIm.getpixel(coordinate) # get the each pixel from the photo in rgba
            rgb = (rgba[0], rgba[1], rgba[2]) # turn it from rgba to only rgb
            im.putpixel((x, y), rgb) # insert the pixel rgb into the map 

    # apply filter multiple times
    for i in range(numiterations):
        im = im.filter(ImageFilter.RankFilter(kernelsize, kernelsize**2 // 2))

    return im





# Libs import
import cv2 as cv
from PIL import Image
import numpy
import matplotlib.pyplot as plt
from pathlib import Path

from read_write import read_image, write_image

"""
    Down there, I used 2 different ways below to solve the exercises
        - CV2
        - PIL
"""
image = read_image('lena.jpg')


def pillow_splitter():
    """
        To divide image into 3 different channels rgb and save them to
        defined path using PILLOW
    """
    ASSET_DIR = (Path(__file__).resolve(
    ).parent.parent.parent).joinpath('assets')
    pillow_img = Image.open(ASSET_DIR.joinpath('lena.jpg'))
    pillow_img_data = pillow_img.getdata()

    # suppress data into 3 different bands represent R-G-B
    r = [(a[0], 0, 0) for a in pillow_img_data]
    g = [(0, a[1], 0) for a in pillow_img_data]
    b = [(0, 0, a[2]) for a in pillow_img_data]

    pillow_img.putdata(r)
    pillow_img.save(ASSET_DIR.joinpath(
        'Exercise01').joinpath('red.png'), 'PNG')

    pillow_img.putdata(g)
    pillow_img.save(ASSET_DIR.joinpath(
        'Exercise01').joinpath('green.png'), 'PNG')

    pillow_img.putdata(b)
    pillow_img.save(ASSET_DIR.joinpath(
        'Exercise01').joinpath('blue.png'), 'PNG')


def histogram_maker(image_file, figure_name):
    # find frequency of intensities in range 0-255
    histr = cv.calcHist([image_file], [0], None, [256], [0, 256])

    # show the plotting graph of an image
    plt.figure()
    plt.title(figure_name)
    plt.xlabel("Levels")
    plt.ylabel("Freq of levels")
    plt.plot(histr)
    plt.show()


# Get histogram for each channel
histogram_maker(cv.imread(
    'D:/My_Work_Space/Image_Processing/Labs_and_Lects/LABS/assets/Exercise01/red.png'), 'RED HISTOGRAM')
histogram_maker(cv.imread(
    'D:/My_Work_Space/Image_Processing/Labs_and_Lects/LABS/assets/Exercise01/green.png'), 'GREEN HISTOGRAM')
histogram_maker(cv.imread(
    'D:/My_Work_Space/Image_Processing/Labs_and_Lects/LABS/assets/Exercise01/blue.png'), 'BLUE HISTOGRAM')

# pillow_splitter()

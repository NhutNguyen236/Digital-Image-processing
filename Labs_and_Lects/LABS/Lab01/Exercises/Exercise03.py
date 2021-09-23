"""
    Exercise 3: Write a program to crop a region of input image and save it to
    another image file by:
"""
import cv2 as cv
import numpy
from PIL import Image
from pathlib import Path

from read_write import read_image

# crop function from pillow


def cropper(image, top, right, bottom, left):
    """
        Cropping image by ratio x and y
        Input: x, y - integers for
        Output: cropped image
    """
    # Setting the points for cropped image
    left = left
    top = top
    right = right
    bottom = bottom

    cropped_img = image.crop((left, top, right, bottom))
    cropped_img.show()


ASSET_DIR = (Path(__file__).resolve(
).parent.parent.parent).joinpath('assets')

image = Image.open(ASSET_DIR.joinpath('lena.jpg'))

cropper(image, 65, 360, 270, 155)

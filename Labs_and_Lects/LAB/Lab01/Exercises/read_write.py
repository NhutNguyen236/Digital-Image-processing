import cv2 as cv
import numpy

from pathlib import Path

def read_image(image_name):
    """
        Read image from defined path with input image
        Input: Image name
        Output: image reading map
    """
    # get assets dir path
    ASSETS_DIR = (Path(__file__).resolve().parent.parent.parent).joinpath('assets')

    # get image exact path and convert to string for imread
    img_src = str(ASSETS_DIR.joinpath(image_name))
    image = cv.imread(img_src)

    return image

def write_image(image_name):
    """
        Write image to a defined path
        Input: Image readind map
    """
    ASSETS_DIR = (Path(__file__).resolve().parent.parent.parent).joinpath('assets')
    written = cv.imwrite('')

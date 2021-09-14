import cv2 as cv
import numpy

from pathlib import Path

# get assets dir path
ASSETS_DIR = (Path(__file__).resolve().parent.parent.parent).joinpath('assets')

# get image exact path and convert to string for imread
img_src = str(ASSETS_DIR.joinpath('lena.jpg'))
image = cv.imread(img_src)
blue, green, red = cv.split(image)

# create a zero matrix with the size of Blue
zeros = numpy.zeros(blue.shape, numpy.uint8)

blueBGR = cv.merge((blue,zeros,zeros))
greenBGR = cv.merge((zeros,green,zeros))
redBGR = cv.merge((zeros,zeros,red))

cv.imshow('Blue Channel', blueBGR)
cv.imshow('Green Channel', greenBGR)
cv.imshow('Red Channel', redBGR)
 
cv.waitKey(0)
cv.destroyAllWindows()
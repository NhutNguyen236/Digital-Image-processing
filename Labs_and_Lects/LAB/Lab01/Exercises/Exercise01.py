import cv2 as cv
import numpy

from read_file import read_image

image = read_image('lena.jpg')
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
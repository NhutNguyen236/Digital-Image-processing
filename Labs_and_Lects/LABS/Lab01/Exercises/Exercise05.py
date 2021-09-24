"""
    Exercise 5: Write a program to overlay a smaller image on a larger image
    using OpenCV library.
"""
import cv2 as cv 
from read_write import read_image

# Read images
peter_image = read_image('Exercise01/Peter.png')
spidey_image = read_image('Exercise01/Spiderman.png')
spider_logo = read_image('Exercise01/spider_logo.png')

def blend_same_size(image1, image2):
    overlay = cv.addWeighted(peter_image, 0.5, spidey_image, 0.7, 0.0)

    cv.imshow('Overlayed', overlay)
    cv.waitKey()
    cv.destroyAllWindows()

def blend_diff_size(image1, image2):
    """
        Overlay images with different sizes
    """
    height, width = (768 , 1024)

    x_offset = int((width - image2.shape[1])/2)
    y_offset = int((height - image2.shape[0])/2)

    image1[ y_offset:y_offset+image2.shape[0], x_offset:x_offset+image2.shape[1]] = image2

    cv.imshow('Overlayed', image1)
    cv.waitKey()
    cv.destroyAllWindows()

print(spider_logo)
blend_diff_size(spidey_image, spider_logo)
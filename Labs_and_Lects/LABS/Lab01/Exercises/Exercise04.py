"""
    Exercise 4: Write a program to draw a rectangle, circle, eclipse shape on
    image and put text Hello world on an input image by OpenCV library.
"""
import cv2 as cv
from read_write import read_image

image = read_image('lena.jpg')


def draw_circle(image):
    """
        Draw circle to the input image
    """
    # center coordinates with coordinates of (0,0) is always at the top right
    # corner of the image
    center_coordinates = (100, 100)

    radius = 20

    # This rules by BGR so this will be red
    color = (0, 0, 255)

    thickness = 100

    circled_img = cv.circle(image, center_coordinates,
                            radius, color, thickness)

    # imshow() only works with waitKey()
    cv.imshow('Circle', circled_img)
    cv.waitKey()


def draw_rectangle(image):
    """
        Draw rectangle to the input image
    """
    # center coordinates with coordinates of (0,0) is always at the top right
    # corner of the image
    start_point = (5, 5)

    end_point = (220, 220)

    # This rules by BGR so this will be red
    color = (0, 0, 255)

    thickness = 2

    rectangle_image = cv.rectangle(
        image, start_point, end_point, color, thickness)

    # imshow() only works with waitKey()
    cv.imshow('Rectangle', rectangle_image)
    cv.waitKey()


def draw_ellipse(image):
    """
        Draw eclipse to the input image
    """
    # center coordinates with coordinates of (0,0) is always at the top right
    # corner of the image
    center_coordinates = (200, 200)

    axesLength = (100, 50)

    angle = 0

    startAngle = 0

    endAngle = 360

    # This rules by BGR so this will be red
    color = (0, 0, 255)

    thickness = 2

    ellipsed_image = cv.ellipse(
        image, center_coordinates, axesLength, angle, startAngle, endAngle, color, thickness)

    # imshow() only works with waitKey()
    cv.imshow('Ellipse', ellipsed_image)
    cv.waitKey()


def texting_img(image):
    # font
    font = cv.FONT_HERSHEY_SIMPLEX

    # org
    org = (50, 50)

    # fontScale
    fontScale = 1

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 2

    # State out message
    message = 'Lena'

    # Using cv2.putText() method
    texted_image = cv.putText(image, message, org, font,
                        fontScale, color, thickness, cv.LINE_AA)

    cv.imshow('Texting', texted_image)
    cv.waitKey()

# The amazing thing here is that opencv will remember the previous state of the image
draw_circle(image)
draw_rectangle(image)
draw_ellipse(image)
texting_img(image)

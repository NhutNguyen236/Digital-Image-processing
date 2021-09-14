#Read, show, save an image and files with cv2
import cv2 as cv
from pathlib import Path

# get assets dir path
ASSETS_DIR = (Path(__file__).resolve().parent.parent).joinpath('assets')

# get image exact path and convert to string for imread
img_src = str(ASSETS_DIR.joinpath('lena.jpg'))
img = cv.imread(img_src)
cv.imshow('Lena Image', img)
cv.waitKey(0)

#Read, show, save an image and files with matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mping

plt.figure()
img = mping.imread(img_src)
plt.imshow(img)
plt.title("Lena Image")
plt.show()

#Read, show, save an image and files with Pillow
from PIL import Image

pil_img = Image.open(img_src)
pil_img.show()
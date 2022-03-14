# import packages
import numpy as np
import argparse
from cv2 import cv2
#some functions that are being worked on so that the program can run regardless of brighntess of image (changes boundaries)
def brightness(image,x,y):
    color = tuple(image[x, y])
    colorbrightness = (color[0]*0.0722)+(color[1]*0.7152)+(color[2]*0.2126)
   # print(color)
    return colorbrightness

def average_brightness(image):
    sum = 0
    count = 0
    for row in range(0,612):
      for col in range(0,408):
        sum = sum + brightness(image,row,col)
        count += 1
    return sum/count
# construct arguments for cli
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "Path Here")
args = vars(ap.parse_args())
# load the image
image = cv2.imread(args["image"])

# define the list of boundaries
boundaries = [
	#([35, 81, 107], [191, 237,  249]),
	([20,94,55], [57+35,189+35,90+ 35]),
	([20, 94, 55], [57+50, 189+50, 90+50]), 
	([20, 94, 55], [57+75, 255, 90+75])#, 
	#([0, 0, 0], [255, 255, 255])
]

# we need a main
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# find colors within the boundaries and apply mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)

	#JAI TESTING
	#Siddharth Testing
	#Beeboss Testing
	#Clickup Testing


#pillow module - pil
# sesha testing macbook reset
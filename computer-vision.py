# import packages
import numpy as np
import argparse
from cv2 import cv2
# construct arguments for cli
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
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
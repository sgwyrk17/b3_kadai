# -*- coding: utf-8 -*-

import cv2
import cv2.cv as cv
import numpy as np

file_path = 'dish1.jpg' 

img = cv2.imread(file_path)
gray_img = cv2.cvtColor(img, cv.CV_RGB2GRAY)
himg = cv2.medianBlur(gray_img,5)

# cimg = cv2.cvtColor(img, cv.CV_GRAY2RGB)
# cv2.imwrite("test.jpg", cimg)

circles = cv2.HoughCircles(himg,cv.CV_HOUGH_GRADIENT,1,20,param1=200,param2=100,minRadius=0,maxRadius=0)
print circles
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
	# draw the outer circle
	# cv2.circle(img,(i[0],i[1]),i[2],(0, 0, 255),3)
	# cut the outer circle
	img = img[i[0]-i[2]:i[0]+i[2], i[1]-i[2]:i[1]+i[2]]

cv2.imwrite("out2_{0}".format(file_path), img)
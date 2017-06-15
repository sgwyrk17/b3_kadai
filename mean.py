# -*- coding: utf-8 -*-

import cv2
import numpy as np
from glob import glob
import re
import os

def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

def compute_mean(dataset):
	sum_image = 0
	for i, image in enumerate(dataset):
		img = cv2.imread(image).astype(np.float32)
		# img = cv2.resize(img, (64, 64)).astype(np.float32)
		# img = img.flatten().astype(np.float32)
		img = np.asarray(img)
		#print i
		#print img
		sum_image += img
	# print sum_image
	# print sum_image / len(dataset)
	return sum_image / len(dataset)

dataset = sorted(glob(os.path.join("../ex3/glasses", "*.jpg")), key=numericalSort)
# print dataset
mean_image = compute_mean(dataset)
cv2.imwrite("glasses_output.jpg", mean_image)
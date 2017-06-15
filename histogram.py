# -*- coding: utf-8 -*-

import numpy as np
import cv2
import pylab as plt

def make_graph(hist1, hist2, hist3, outpath):
	plt.figure()
	plt.subplot(3, 1, 1)
	plt.plot(hist1, "b")
	plt.xlim(0, 256)

	plt.subplot(3, 1, 2)
	plt.plot(hist2, "g")
	plt.xlim(0, 256)

	plt.subplot(3, 1, 3)
	plt.plot(hist3, "r")
	plt.xlim(0, 256)

	plt.savefig(outpath)

if __name__ == '__main__':
	image = "./dark.jpg"
	img = cv2.imread(image)
	img_blue_c1, img_green_c1, img_red_c1 = cv2.split(img)

	hist_blue, bins_blue = np.histogram(img_blue_c1, bins=256)
	hist_green, bins_green = np.histogram(img_green_c1, bins=256)
	hist_red, bins_red = np.histogram(img_red_c1, bins=256)

	make_graph(hist_blue, hist_green, hist_red, "histogram1.jpg")

	# blue
	cdf_blue = hist_blue.cumsum()
	cdf_blue = 255 * cdf_blue / cdf_blue[-1]
	img_blue_c2 = np.interp(img_blue_c1, bins_blue[:-1], cdf_blue)

	# green
	cdf_green = hist_green.cumsum()
	cdf_green = 255 * cdf_green / cdf_green[-1]
	img_green_c2 = np.interp(img_green_c1, bins_green[:-1], cdf_green)

	# red 
	cdf_red = hist_red.cumsum()
	cdf_red = 255 * cdf_red / cdf_red[-1]
	img_red_c2 = np.interp(img_red_c1, bins_red[:-1], cdf_red)

	hist_blue2, bins_blue = np.histogram(img_blue_c2, bins = 255)
	hist_green2, bins_green = np.histogram(img_green_c2, bins = 255)
	hist_red2, bins_red = np.histogram(img_red_c2, bins =255)

	make_graph(hist_blue2, hist_green2, hist_red2, "histogram2.jpg")

	img_flat = cv2.merge((img_blue_c2, img_green_c2, img_red_c2))
	# cv2.show(img_flat)
	cv2.imwrite("dark_flat.jpg", img_flat)

import numpy as np
import cv2

class Descriptor:
	def __init__(self, bins):
		self.bins = bins

	def describe(self, image):
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)		# Converting the RGB image to HSV colour space
		features = []		# Array of features for the given image
		(height, width) = image.shape[:2]		# Dimensions of the image
		(centreX, centreY) = (int(width * 0.5), int(height * 0.5))		# Centre of the image

		segments = [(0, centreX, 0, centreY), (centreX, width, 0, centreY), (centreX, width, centreY, height),
			(0, centreX, centreY, height)]		# Divide the image into 4 segments (quadrants)

		# construct an elliptical mask of 75% dimensions representing the central segment of the image
		(axesX, axesY) = (int(width * 0.75) / 2, int(height * 0.75) / 2)
		elliptical_mask = np.zeros(image.shape[:2], dtype = "uint8")		# Mask of dimensions of image
		cv2.ellipse(elliptical_mask, (centreX, centreY), (axesX, axesY), 0, 0, 360, 255, -1)		# Making ellipse on the mask

		# Making 5 segments by subtracting overlapping areas
		for (startX, endX, startY, endY) in segments:
			FullMask = np.zeros(image.shape[:2], dtype = "uint8")
			cv2.rectangle(FullMask, (startX, startY), (endX, endY), 255, -1)
			Subtracted_Mask = cv2.subtract(FullMask, elliptical_mask)		# Removing part common with ellipse
			hist = self.histogram(image, Subtracted_Mask)		# Obtaining the histogram for this segment
			features.extend(hist)

		hist = self.histogram(image, elliptical_mask)	# Obtaining histogram for central elliptical region
		features.extend(hist)

		return features		# Returning the bag of words for this image

	def histogram(self, image, mask):
		hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins, [0, 180, 0, 256, 0, 256])		# Obtaining the HSV histogram
		hist = cv2.normalize(hist,hist).flatten()		# Normalizing the histogram
		return hist
# assumes index.csv is in the same directory
import numpy as np
import csv

class Searcher:
	def search(self, queryWords, limit = 10):
		results = {}		#We will store the names of the matching images in this array

		# open the index file for reading
		with open("index.csv") as index_file:
			reader = csv.reader(index_file)		# initialize the CSV reader

			for row in reader:
				features = [float(x) for x in row[1:]]		# 0th element of every row is the name of the image, so we start from the 1st element
				distance = self.chi2_distance(features, queryWords)	# Computing the chi-squared distance between the Bag of words in test image and current dataset image
				results[row[0]] = distance 	# row[0] contains the name of the image, d contains the measure of similarity (distance)

			index_file.close()

		results = sorted([(v, k) for (k, v) in results.items()])	# sorting results on the basis of smallest distance between images (best matches)

		return results[:limit]		# returning only 10 best matches

	def chi2_distance(self, histA, histB, eps = 1e-10):				# compute the chi-squared distance
		chi = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)		# we calculate the cumulative distance between the histograms as the sum of individual point distances
			for (a, b) in zip(histA, histB)])		# zip combines all the pairs of elements of the histograms into one array
		return chi
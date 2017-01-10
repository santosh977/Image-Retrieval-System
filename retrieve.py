# assumes index.csv is in the current directory
# USE: python retrieve.py --image queries/103100.png --data_path dataset

from descriptor import Descriptor
from searcher import Searcher
import argparse
import cv2

# construct the argument parser and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-q", "--image", required = True,
	help = "Path to the test image")
parser.add_argument("-r", "--data_path", required = True,
	help = "Path to the dataset")
arguments = vars(parser.parse_args())

test = cv2.imread(arguments["image"])	#reading the test image
searcher = Searcher()	#initialising the searcher object

desc = Descriptor((8, 12, 3))	#initialising the descriptor
words = desc.describe(test)	#obtaining the features (bag of visual words) of the test image

results = searcher.search(words)		#results obtained by searching in the dataset

# display the test
cv2.imshow("Test image", test)

pp = 1

# loop over the results
for (score, ID) in results:
	result = cv2.imread(arguments["data_path"] + "/" + ID)
	cv2.imshow("Result " + `pp`, result)
	if pp == 5:
		cv2.waitKey(0)
	pp += 1
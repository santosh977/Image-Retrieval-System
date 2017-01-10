# USE : python index.py --data_path dataset

# import the necessary packages
from descriptor import Descriptor
import argparse
import glob
import cv2

# construct the argument parser and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--data_path", required = True,
	help = "Path to the directory that contains the images to be indexed")
arguments = vars(parser.parse_args())

desc = Descriptor((8, 12, 3))
index_file = open("index.csv", "w")		# opening the index.csv file for writing

# use glob to grab the image paths and loop over them
for imagePath in glob.glob(arguments["data_path"] + "/*.png"):
	ID = imagePath[imagePath.rfind("/") + 1:]		# Name of the image
	image = cv2.imread(imagePath)

	features = desc.describe(image)	# getting the bag of words for the image

	words = [str(f) for f in features]		# Combining the features to form a bag of words
	index_file.write("%s,%s\n" % (ID, ",".join(words)))		# Writing in the csv file (comma required because comma separated values (csv) files)

index_file.close()
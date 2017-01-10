IMAGE RETREIVAL SYSTEM:

Installation Requirements :
	Platform:
		ubuntu
	Tools:
		python
	Dependencies:
		Following python libraries are required : cv2, numpy, csv, argparse, glob

	Details of Dataset :
		The folder "Dataset" should contain only images.
		We used a major portion of INRIA holiday dataset as mentioned in the assignment problem statement.
	

Usage Instructions :
	For indexing the given set of images(dataset) contained in subfolder dataset/, use the following commad:
		python index.py --data_path dataset

	For retreiving images similar to the query image run the following command:
		python retrieve.py --image query.png --data_path dataset

Get our Results:
 	Use query images in the Test folder
	python retrieve.py --image Test/test.png --data_path dataset    //	Replace test.png with the actual image file

References :
(1) http://en.wikipedia.org/wiki/Bag-of-words_model_in_computer_vision
(2) http://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/
(3) http://www.researchgate.net/post/What_is_chi-squared_distance_I_need_help_with_the_source_code
(4) http://vlm1.uta.edu/~athitsos/publications/athitsos_icde2008.pdf
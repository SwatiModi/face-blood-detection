import cv2
import numpy as np
import glob


imagePath = glob.glob("blood_faces/*.jpg")
blood = 0
no_blood = 0

for images in imagePath:
	image = cv2.imread(images)

	try : 

		size = image.shape[0]*image.shape[1]
		print(size)

		if size < 15000:
			continue
		
		red = np.uint8(image)
		hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
		# print(hsv_red)

		# define the list of boundaries
		boundaries = [
			([17, 15, 100], [50, 56, 200]),
			([86, 31, 4], [220, 88, 50]),
			([25, 146, 190], [62, 174, 250]),
			([103, 86, 65], [145, 133, 128])
		]

		# loop over the boundaries
		for (lower, upper) in boundaries:
			# create NumPy arrays from the boundaries
			lower = np.array(lower, dtype = "uint8")
			upper = np.array(upper, dtype = "uint8")
		 
			# find the colors within the specified boundaries and apply
			# the mask
			mask = cv2.inRange(image, lower, upper)
			output = cv2.bitwise_and(image, image, mask = mask)

			# count red pixels
			red = np.count_nonzero(output)

			# find total no. of pixels
			width, height,c = output.shape

			total = width*height
			print(total)

			# calculate the percent of red pixels in the image
			percent = red/total
			print(percent)


			# if percent of red pixels is greater then threshold, classify as blood_face 
			if round(percent,3) > 0.01:
				print('blood face')
				blood = blood + 1
			else:
				print('no blood face')
				no_blood = no_blood + 1

			# show the images
			# cv2.imshow("images", np.hstack([image, output]))
			# cv2.waitKey(0)

	except :
		pass

acc = blood/(blood+no_blood)
print(f'Accuracy',acc)

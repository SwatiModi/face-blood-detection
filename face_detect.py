import cv2
import sys
import glob

# Get user supplied values
imagePath = glob.glob("blood/*.jpg")
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

for images in imagePath:
	try:
		# Read the image
		image = cv2.imread(images)

		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		# Detect faces in the image
		faces = faceCascade.detectMultiScale(
		    gray,
		    scaleFactor=1.1,
		    minNeighbors=3,
		    minSize=(30, 30),
		    flags = cv2.CASCADE_SCALE_IMAGE
		)

		print("Found {0} faces!".format(len(faces)))

		if len(faces) == 0:
			cv2.imwrite('blood_faces/' +  str(images[6:]), image)

		i = 0

		# Draw a rectangle around the faces
		for (x, y, w, h) in faces:
			i = i + 1
			cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
			roi = image[y:y+h, x:x+w]
			cv2.imwrite('blood_faces/' + str(i) + '_' +str(images[6:]), roi)

		# cv2.imshow("Faces found", image)
		# cv2.waitKey(0)
	except:
		print(str(images))
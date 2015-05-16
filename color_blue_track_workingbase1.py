import numpy as np 
import cv2 

cap = cv2.VideoCapture(0)

#range for blue
lower_blue = np.array([110, 100, 100])
upper_blue = np.array([130, 255, 255])

# kernel for opening and dilating
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))


while(cap.isOpened()):

	_, frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	mask = cv2.inRange(hsv, lower_blue, upper_blue)


	# Opening to remove noise
	bluethresh_open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	bluethresh_dilate = cv2.dilate(bluethresh_open, kernel, iterations = 2)


	cv2.imshow("frame", bluethresh_dilate)

	if cv2.waitKey(1) & 0xff == 27:
		break

cap.release()
cv2.destoyAllWindows()




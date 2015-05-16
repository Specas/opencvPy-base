import numpy as np 
import cv2 

cap = cv2.VideoCapture(0)

#range for blue
lower_white = np.array([0, 0, 110])
upper_white = np.array([170, 50, 255])

# kernel for erosion
kernel = np.ones((2,2), np.uint8)
kernel_ell = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))


while(cap.isOpened()):

	_, frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	mask = cv2.inRange(hsv, lower_white, upper_white)

	mask_open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_ell)
	mask_dilate = cv2.dilate(mask_open, kernel_ell, iterations = 1)



	cv2.imshow("frame", mask_dilate)

	if cv2.waitKey(1) & 0xff == 27:
		break

cap.release()
cv2.destoyAllWindows()




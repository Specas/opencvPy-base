import numpy as np 
import cv2

cap = cv2.VideoCapture(0)

kernel_ell1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
kernel_ell2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(1,1))

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(2000,5,0.01,0)

while cap.isOpened():

	_, frame = cap.read()

	frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	fgmask = fgbg.apply(frame_hsv)
	fgmask_open = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel_ell1)
	fgmask_open = cv2.morphologyEx(fgmask_open, cv2.MORPH_CLOSE, kernel_ell2)

	cv2.imshow("frame", fgmask_open)

	if cv2.waitKey(1) & 0xff == 27:
		break
cap.release()
cv2.destroyAllWindows()
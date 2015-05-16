import numpy as np 
import cv2

cap = cv2.VideoCapture(0)
is_first_frame = True
frame1 = []
frame2 = []
while(cap.isOpened()):
	_, frame = cap.read()

	if is_first_frame:
		frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		is_first_frame = False # no longer the first frame
	else:
		frame1 = frame2
		frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# after this frame2 stores the current frame and frame1 stores the previous frame

	_, frame1thresh = cv2.threshold(frame1, 127, 255, cv2.THRESH_BINARY)
	_, frame2thresh = cv2.threshold(frame2, 127, 255, cv2.THRESH_BINARY)
	frame2thresh = cv2.bitwise_not(frame2thresh)

	

	finalframethresh = cv2.bitwise_and(frame1thresh, frame2thresh)
	#finalframethresh = cv2.medianBlur(finalframethresh, 7)



	cv2.imshow("frame", finalframethresh)
	
	if cv2.waitKey(1) & 0xFF == 27:
			break
cap.release()
cv2.destroyAllWindows()



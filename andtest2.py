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
	#using canny edge on frame1 and frame2

	frame1canny = cv2.Canny(frame1, 100, 200)
	frame2canny = cv2.Canny(frame2, 100, 200)
	frame2canny = cv2.bitwise_not(frame2canny)

	kernel = np.ones((5,5), np.uint8)

	finalframecanny = cv2.bitwise_and(frame1canny, frame2canny)
	finalframcanny = cv2.morphologyEx(finalframecanny, cv2.MORPH_OPEN, kernel)
	cv2.imshow("final", finalframecanny)





	if cv2.waitKey(1) & 0xFF == 27:
		break
cap.release()
cv2.destroyAllWindows()
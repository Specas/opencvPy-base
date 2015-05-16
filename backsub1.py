import numpy as np
import cv2

cap = cv2.VideoCapture(0)
kernel1 = np.ones((2,2), np.uint8)
kernel2 = np.ones((4,4), np.uint8)

kernel_ell1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
kernel_ell2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(1,1))

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(20000,5,0.0001,0)
# fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = False)

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
    fgmask_open = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel_ell1)
    fgmask_open = cv2.morphologyEx(fgmask_open, cv2.MORPH_CLOSE, kernel_ell2)
	


    cv2.imshow('frame',fgmask_open)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
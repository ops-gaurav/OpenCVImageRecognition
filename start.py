import numpy as np
import cv2

cap = cv2.VideoCapture(0)


while(True):
	# capture frame by frame
	ret, frame = cap.read()

	# implement the frame operations here
	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# display the frame
	cv2.imshow('frame', frame)
	# cv2.imshow('gray', gray)

	if cv2.waitKey(20) & 0XFF == ord('q'):
		break

# when everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
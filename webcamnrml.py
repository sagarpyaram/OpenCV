import cv2
cam=cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2(history=20, varThreshold=100, detectShadows=True)
k=0
count=0
while True:
    ret , frame = cam.read()
    cv2.imshow("img",frame)
    if cv2.waitKey(3)==ord('q'):
        break;
cam.release()
cv2.destroyAllWindows()


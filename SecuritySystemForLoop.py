import cv2
#camera object
cam=cv2.VideoCapture(0)
count=0
fgbg = cv2.createBackgroundSubtractorMOG2(history=0,varThreshold=10,detectShadows=True)
while True:
    ret,frame=cam.read()
    row,col,z=frame.shape
    x=int(row/2)
    y=int(col/2)
    fgmask = fgbg.apply(frame)
    cv2.imshow("img",frame)
    #cv2.imshow("img2",ret)    
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    for i in range (x):
        for j in range (y):
           # print(fgmask[i,j])
            h=fgmask[i,j]            
            if (h!=0 ):
                count=count+1
    count=fgmask[100,100,100]
    if count>=((x*y)/100):
        print("alarm")
    else:
        print("pass")
    count=0
    if cv2.waitKey(3)==ord('q'):#q or k==27:
        break;

    
cam.release()

cv2.destroyAllWindows()
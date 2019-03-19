import cv2
#Camera object
cam=cv2.VideoCapture(0)
while True:
    ret , frame = cam.read()
    #frame=cv2.resize(frame,(600,480),interpolation=cv2.INTER_AREA)
    a,b,c=frame.shape
    x=int(a)
    y=int(b)
    m=int(a/2)
    n=int(b/2)
    print(a,b)
    #Crosshair
    #cv2.circle(frame,(y,x),2,(0,0,255),-1)
    
    cv2.rectangle(frame,(0,0),(648,160),(0,128,255),-1)
    cv2.rectangle(frame,(0,160),(648,320),(255,255,255),-1)
    cv2.rectangle(frame,(0,320),(648,480),(0,153,76),-1)
    cv2.circle(frame,(n,m),79,(255,0,0),2)
    #cv2.line(frame,(y-12,x),(y+12,x),(0,0,255),1)
    #cv2.line(frame,(y,x-12),(y,x+12),(0,0,255),1)
    #Crosshair End
    cv2.imshow("img",frame) 
    if cv2.waitKey(3)==ord('q'):
        break;
cam.release()
cv2.destroyAllWindows()


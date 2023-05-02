import cv2
import dlib

cap=cv2.VideoCapture(0)

detector=dlib.get_frontal_face_detector()

while(True):
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    i=0
    for face in faces:
        x,y = face.left() , face.top()
        x1,y1 = face.right() , face.bottom()
        cv2.rectangle(frame, (x,y) ,(x1,y1),(0,255,0),2)
        i +=1
        cv2.putText(frame,str(i),(x-15,y-15),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow('frame',frame)
    k = cv2.waitKey(100) & 0xff

    if k == 27:
        break

print("\n Hoan Thanh")
cam.release()
cv2.destroyAllWindows()  # hủy


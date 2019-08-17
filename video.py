import cv2

video = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcarcde_face_front.xml')

a=1

while True:
    a +=1
    check, frame = video.read()
    print(frame)
     
    gray = cv2.cvtColor(frame,cv2.COLOR_BGRA2GRAY)

    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)

    for x,y,w,h in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        roi_gray = gray[y:y+h,x:x+w]
        img_out = "out_img.png"
        cv2.imwrite(img_out,roi_gray)

    cv2.imshow("img",frame)

    


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()
import cv2

face_cascade = cv2.CascadeClassifier("haarcarcde_face_front.xml")

img = cv2.imread("faces.jpg",1)

img_gray =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(img_gray, scaleFactor=1.05, minNeighbors=5)

for x,y,w,h in face:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

cv2.imshow("face",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(type(face))
print(face)


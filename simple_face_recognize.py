import cv2
import numpy as np

img_color = cv2.imread('C:\Users\samsung\PycharmProjects\project1\people.jpg', cv2.IMREAD_COLOR)
gray_image = cv2.cvtColor(img_color,cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier('C:\Users\samsung\PycharmProjects\project1\haar_face.xml')
faces = faceCascade.detectMultiScale(
    gray_image,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(20,20),
)


#faces에 담긴 것을 xywh 에 나눠서 할당 하고 사각혁을 받아서 그린다. faces 에는 이미 분류를 통한 객체 사각혀잉 있다.
print "FIND {0} faces!!".format(len(faces))
for (x,y,w,h) in faces:
    cv2.rectangle(gray_image, (x,y), (x+w, y+h), (100,255,200), 2)

cv2.imshow("face",gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

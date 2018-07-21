import cv2
import numpy as np

img_color = cv2.imread('C:\Users\samsung\PycharmProjects\project1\project1\people.jpg', cv2.IMREAD_COLOR)
gray_image = cv2.cvtColor(img_color,cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier('C:\Users\samsung\PycharmProjects\project1\project1\haar_face.xml')
faces = faceCascade.detectMultiScale(
    gray_image,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(20,20),
)


print "FIND {0} faces!!".format(len(faces))
for (x,y,w,h) in faces:
    cv2.rectangle(gray_image, (x,y), (x+w, y+h), (100,255,200), 2)

cv2.imshow("face",gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

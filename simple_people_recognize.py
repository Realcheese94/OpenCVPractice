
import cv2
import os
import numpy as np

image = cv2.imread('C:\Users\samsung\PycharmProjects\project1\project1\Bodybody.jpg', cv2.IMREAD_COLOR)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
body_cascade = cv2.CascadeClassifier('C:\Users\samsung\PycharmProjects\project1\project1\haarcascade_fullbody.xml')
bodys = body_cascade.detectMultiScale(
    gray_image,


)
print "find {0} body".format(len(bodys))

for (x,y,w,h) in bodys:
    cv2.rectangle(gray_image, (x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("hi",gray_image)
cv2.waitKey(0)
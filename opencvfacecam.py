#coding=utf-8  
import cv2
url = 'http://admin:admin@192.168.31.149:8081/'
videoCapture = cv2.VideoCapture(url)
while 1 :
	set,frame = videoCapture.read()
	cv2.imshow('Video', frame)
cv2.destroyAllWindows()
import cv2 
import numpy as np  
img = cv2.imread("D:/python/img/1.jpg")
width,height,dtype = img.shape
print(width)
print(height)
print(dtype)
width1 = int(width/2);
height1 = int(height/2)
print(width1)
print(height1)
cv2.putText(img, 'Hello World', (300,100), 0, 0.5, (0,0,255),2)
cv2.imshow('Hello World', img)
img1 = cv2.resize(img,(height1,width1),interpolation=cv2.INTER_NEAREST)
cv2.imshow('expand',img1)
img2 = cv2.resize(img,(height1,width1),interpolation=cv2.INTER_LINEAR)
cv2.imshow('expand1',img2)
img3 = cv2.resize(img,(height1,width1),interpolation=cv2.INTER_AREA)
cv2.imshow('expand2',img3)
M = np.array([[1,0,50],[0,1,50]],np.float32)
img_str = cv2.warpAffine(img3,M,img3.shape[:2])
cv2.imshow('aff',img_str)
M1 = cv2.getRotationMatrix2D((width1,height1),45,1)
img_ro = cv2.warpAffine(img,M1,img.shape[:2])
cv2.imshow('rotation',img_ro)
cv2.waitKey(0)
cv2.destroyAllWindows()

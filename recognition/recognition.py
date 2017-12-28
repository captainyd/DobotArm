import numpy as np
import cv2

img = cv2.imread('sample_5.jpg')
img =cv2.resize(img,(800,600),interpolation=cv2.INTER_CUBIC)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blur = cv2.blur(gray,(0, 0));
# cv2.imshow('blur',gray)
ret,thresh = cv2.threshold(gray,127,255,1)
# cv2.imshow('ret',thresh)
_,contours,h = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img,contours,-1,(0,255,255),3)
# cv2.imshow('cnt',img)

figure = []

for cnt in contours:
	# print (cnt)
	approx = cv2.approxPolyDP(cnt,0.05*cv2.arcLength(cnt,True),True)
	r = len(approx)
	# print (approx)
	if len(approx)==5:
		print ("pentagon")
		cv2.drawContours(img,[cnt],0,255,2)
	elif len(approx)==3:
		print ("triangle")
		cv2.drawContours(img,[cnt],0,(0,255,0),2)
		figure = figure + [approx]
	elif len(approx)==4:
		print ("square")
		figure = figure + [approx]
		cv2.drawContours(img,[cnt],0,(0,0,255),2)
	elif len(approx) == 9:
		print ("half-circle")
		cv2.drawContours(img,[cnt],0,(255,255,0),2)
	elif len(approx) > 15:
		print ("circle")
		cv2.drawContours(img,[cnt],0,(0,255,255),2)

print (figure[0])
print (figure[1])

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

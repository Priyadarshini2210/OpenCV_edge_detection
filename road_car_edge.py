import cv2
import imutils
import numpy

img=cv2.imread("cars.jpeg")
cv2.imshow("image",img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayshow=cv2.imshow("GrayImage", gray)
cv2.waitKey(0)


edge=cv2.Canny(gray , 50,170)
cv2.imshow("edge show" , edge)
cv2.waitKey(0)

edge2=cv2.Canny(gray , 30,150)
cv2.imshow("edge show2" , edge2)
cv2.waitKey(0)

edge3=cv2.Canny(gray , 165,170)
cv2.imshow("edge show3" , edge3)
cv2.waitKey(0)			
cv2.imwrite("edge_img_road_car.jpg" , edge3)	


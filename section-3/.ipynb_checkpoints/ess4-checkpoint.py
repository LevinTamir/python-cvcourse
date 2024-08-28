import numpy as np
import matplotlib.pyplot as plt
import cv2

## FUNCTION
def draw_circle(event,x,y,flags,param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(circle_img,(x,y),100,(0,0,255),thickness=10)


## SHOWING IMAGE WITH OPENCV
circle_img = cv2.imread('../DATA/dog_backpack.png')

cv2.namedWindow(winname='dog')
cv2.setMouseCallback('dog',draw_circle)

while True:
    
    cv2.imshow('dog',circle_img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
        
cv2.destroyAllWindows()

import numpy as np
from cv2 import cv2

import pyperclip

def rgb_to_hex(rgb):
    
    return '%02x%02x%02x' % rgb  #converting rgb to hex



def click_event(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        blue= img[y,x,0]  
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = '#'+ str(rgb_to_hex((red,blue,green)))  
        pyperclip.copy(strXY)
        cv2.putText(img, strXY, (x, y),font, 1, (0,0,0), 2)
        cv2.imshow('image', img)



img = cv2.imread("Just Slide.png", 1)   #dir of image
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

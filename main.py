#!/usr/bin/env python3

import sys
import numpy as np
from cv2 import cv2
import pyperclip

if len(sys.argv) == 1:
	picture = 'Just Slide.png'
else:
	picture = sys.argv[1]
img = cv2.imread(picture)

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb	# Converts RGB to Hex. RGB is passed as a tuple.

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue= img[y, x, 0]  
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = '#' + str(rgb_to_hex((red,blue,green)))  
        pyperclip.copy(strXY)
        cv2.putText(img, strXY, (x, y), font, 1, (0, 0, 0), 2)
        cv2.imshow(picture, img)

cv2.imshow(picture, img)
cv2.setMouseCallback(picture, click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

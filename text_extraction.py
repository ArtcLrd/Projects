import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr
import down

res = "NULL"

class image_mod:
    
    def __init__(self,x):
        path = x
        image_mod.mod(self,x)

    def mod(self,x):
        global res
        img = cv2.imread(x)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        bf = cv2.bilateralFilter(gray,11,17,17)
        kp = cv2.findContours(gray.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        con= imutils.grab_contours(kp)
        con = sorted(con, key=cv2.contourArea, reverse=True)[:10]
        mask = np.zeros(gray.shape, np.uint8)
        loc = None
        for contour in con:
            approx = cv2.approxPolyDP(contour, 10, True)
            if (len(approx) == 4):
                loc = approx
                break
        new_img = cv2.drawContours(mask, [loc], 0,255,-1)
        new_img = cv2.bitwise_and(img, img, mask=mask)
        image_mod.extract_text(self,new_img)

    def extract_text(self,n):
        global res
        reader = easyocr.Reader(['en'])
        result = reader.readtext(n,detail=0)
        print(result)
        if not len(result)==0 and not result[0]=='':
            res = (result[0])
            print(result[0])
        elif len(result)==0:
            res = "NULL"   
        else:
            res="NULL"
    def ret_str(self):
        global res
        
        return res
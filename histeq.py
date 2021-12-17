import cv2
import imutils
import numpy as np

def import_img():
    img = cv2.imread("BW_test.jpg")
    img = imutils.resize(img,width=512)
    return img

def eqhist(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(img)
    comp = np.hstack((img,equ))
    cv2.imshow("comparison",comp)
    cv2.waitKey()

IMG=import_img()
eqhist(IMG)
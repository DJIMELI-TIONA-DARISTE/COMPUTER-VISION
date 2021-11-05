import cv2 as cv
import numpy as np
from  skimage import  io
from  matplotlib import  pyplot as plt
img = cv.imread("imageTP1/tp1_3.png")

R, G, B = cv.split(img)

output1_R = cv.equalizeHist(R)
output1_G = cv.equalizeHist(G)
output1_B = cv.equalizeHist(B)
equ = cv.merge((output1_R, output1_G, output1_B))
cv.imshow("img-3", equ)
plt.hist(equ.ravel(), 256, [0, 256])
plt.show()

cv.waitKey(0)
cv.destroyWindow()


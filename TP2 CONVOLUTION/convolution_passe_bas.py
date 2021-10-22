import numpy as np
import cv2

#read image
img_src = cv2.imread('imageTP2/tp2_4.png')

#prepare the 5x5 shaped filter
kernel = np.array([[1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1]])
kernel = kernel/sum(kernel)

#filter the source image
img_rst = cv2.filter2D(img_src,-1,kernel)
cv2.imshow("origin",img_src)
cv2.imshow("result",img_rst)
cv2.waitKey(0)
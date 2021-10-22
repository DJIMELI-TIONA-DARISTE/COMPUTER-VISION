import numpy as np
import cv2

#read image
img_src = cv2.imread("imageTP2/tp2_3.png")

#edge detection filter
kernel = np.array([[0.0, -1.0, 0.0],
                   [-1.0, 4.0, -1.0],
                   [0.0, -1.0, 0.0]])

kernel = kernel/(np.sum(kernel) if np.sum(kernel)!=0 else 1)
#filter the source image
img_rst = cv2.filter2D(img_src,-1,kernel)
#show image
cv2.imshow("original", img_src)
cv2.imshow("Filtre passe haut 3*3",img_rst)
cv2.waitKey(0)
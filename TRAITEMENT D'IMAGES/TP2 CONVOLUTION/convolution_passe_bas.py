import numpy as np
import cv2

#Lecture de l'image source
img_src = cv2.imread('imageTP2/tp2_1.png')

#Définition de filtre passe-bas 5*5
kernel = np.array([[1, 1, 1, 1, 1, ],
                   [1, 1, 1, 1, 1, ],
                   [1, 1, 1, 1, 1, ],
                    [1, 1, 1, 1, 1, ],
                   [1, 1, 1, 1, 1, ]])
kernel = kernel/sum(kernel)

#filtrer l'image source
img_rst = cv2.filter2D(img_src,-1,kernel)
cv2.imshow("origin",img_src)
cv2.imshow("result 3 * 3 ",img_rst)
cv2.waitKey(0)
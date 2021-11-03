import numpy as np
import cv2

#Lecture de l'image
img_src = cv2.imread("imageTP2/tp2_4.png")

# définition du filtre
kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])

kernel = kernel/(np.sum(kernel) if np.sum(kernel)!=0 else 1)
#filtrer l'image
img_rst = cv2.filter2D(img_src,-1,kernel)

#aperçu de l'image d'origine et l'image filtrée
cv2.imshow("original", img_src)
cv2.imshow("image_convolue ",img_rst)
cv2.waitKey(0)
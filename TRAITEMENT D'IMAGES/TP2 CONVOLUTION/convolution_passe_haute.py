import numpy as np
import cv2

#Lecture de  l'image
img_src = cv2.imread("imageTP2/tp2_3.png")

#Définition du filtre passe-haut
kernel = np.array([[0, -1.0, 0.0],
                   [-1.0, 4.0, -1.0],
                   [0.0, -1.0, 0.0]])

kernel = kernel/(np.sum(kernel) if np.sum(kernel)!=0 else 1)
#filtrer l'image source
img_rst = cv2.filter2D(img_src,-1,kernel)
#aperçu de l'image
cv2.imshow("original", img_src)
cv2.imshow("Filtre passe haut 3*3",img_rst)
cv2.waitKey(0)
import numpy as np
import cv2

#lecture de l'image
img = cv2.imread("imageTP2/tp2_3.png")

# Définition des différents filtres
G_X = np.array([[1, 1, 1],
                [0, 0, 0],
                [-1, -1, -1]])

G_Y = np.array([[-1, 0, 1],
                [-1, 0, 1],
                [-1, 0, 1]])
G_X = cv2.filter2D(img, -1, G_X)
G_Y = cv2.filter2D(img, -1, G_Y)

#aperçu  des images

cv2.imshow("original", img)
cv2.imshow("G_x",G_X)
cv2.imshow("G_Y",G_Y)
cv2.imshow("prewitt_resultant", G_X + G_Y)
cv2.waitKey(0)
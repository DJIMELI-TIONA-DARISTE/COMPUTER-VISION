import cv2
import numpy as np
from  matplotlib import  pyplot as plt


def gammaCorrection(src, gamma):
    invGamma = 1 / gamma

    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(src, table)


img = cv2.imread('imageTP1/tp1_2.png')
gammaImg = gammaCorrection(img, 3)

cv2.imshow('Correction Gamma image-4', gammaImg)

plt.hist(gammaImg.ravel(), 256, [0, 256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
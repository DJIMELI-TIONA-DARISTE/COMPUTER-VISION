import  numpy as np
import  cv2 as cv
from  matplotlib import  pyplot as plt
image = cv.imread("imageTP1/tp1_3.png")
cv.imshow("img-3", image)
plt.hist(image.ravel(), 256, [0, 256])
plt.show()

cv.waitKey(0)
cv.destroyWindow()
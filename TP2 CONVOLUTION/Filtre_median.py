import cv2
from skimage.filters import median


img_salt_pepper_noise = cv2.imread('imageTP2/SaltPepper.png', 0)

img = img_salt_pepper_noise


median_using_cv2 = cv2.medianBlur(img, 3)

from skimage.morphology import disk
#Disk creates a circular structuring element, similar to a mask with specific radius
median_using_skimage = median(img, disk(3), mode='constant', cval=0.0)


cv2.imshow("Original", img)
cv2.imshow("cv2 median", median_using_cv2)
cv2.imshow("Median Filter", median_using_skimage)

cv2.waitKey(0)
cv2.destroyAllWindows()
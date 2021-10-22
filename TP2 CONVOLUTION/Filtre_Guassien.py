import cv2
from skimage import io, img_as_float
from skimage.filters import gaussian

img_gaussian_noise = img_as_float(io.imread('imageTP2/SaltPepper.png', as_gray=True))

img = img_gaussian_noise

gaussian_using_cv2 = cv2.GaussianBlur(img, (7,7), 0, borderType=cv2.BORDER_CONSTANT)

cv2.imshow("Original", img)
cv2.imshow("Gaussian 3 * 3", gaussian_using_cv2)

cv2.waitKey(0)
cv2.destroyAllWindows()
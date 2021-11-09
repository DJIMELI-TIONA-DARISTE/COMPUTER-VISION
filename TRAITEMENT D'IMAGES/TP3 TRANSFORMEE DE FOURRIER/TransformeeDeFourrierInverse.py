import numpy as np
import cv2
from matplotlib import pyplot as plt
#Lecture de l'image
img = cv2.imread("imageTP3/tp2_2.png",0)

#Transformee de fourrier
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
spectre = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

#Transformee de fourrier inverse
magnetude, phase = cv2.cartToPolar(dft_shift[:,:,0], dft_shift[:,:,1])
real, imag = cv2.polarToCart(magnetude, phase)
retour = cv2.merge([real, imag])
retour_ishift = np.fft.ifftshift(retour)
img_retour = cv2.idft(retour_ishift)
img_retour = cv2.magnitude(img_retour[:, :, 0], img_retour[:, :, 1])
min, max = np.amin(img_retour, (0, 1)), np.amax(img_retour, (0, 1))
print(min,max)
img_retour = cv2.normalize(img_retour, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

cv2.imshow("image_retour", img_retour)
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title("Image d'origine"), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(spectre, cmap = 'gray')
plt.title("Spectre"), plt.xticks([]), plt.yticks([])
plt.show()
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("imageTP3/tp2_3.png",0)

dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

spectre = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))


plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title("Image d'origine"), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(spectre, cmap = 'gray')
plt.title("Spectre"), plt.xticks([]), plt.yticks([])
plt.show()
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("imageTP3/tp2_4.png",0)

dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

spectre = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))


#masque circulaire pass-bass,
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
mask = np.zeros((rows, cols, 2), np.uint8)
r_out = 96
r_in = 0
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
mask_area = np.logical_and(((x - center[0]) ** 2 + (y - center[1]) ** 2 >= r_in ** 2),
                           ((x - center[0]) ** 2 + (y - center[1]) ** 2 <= r_out ** 2))
mask[mask_area] = 1

# on applique masque et calcul la transformee inverse de fourrier
fshift = dft_shift * mask
fshift_mask_mag = 2000 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

#transformee inverse de fourrier
f_ishift = np.fft.ifftshift(fshift)
img_retour = cv2.idft(f_ishift)
img_retour = cv2.magnitude(img_retour[:, :, 0], img_retour[:, :, 1])

#affichage des différents résultats
fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img, cmap='gray')
ax1.title.set_text("Image d'origine")
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(spectre, cmap='gray')
ax2.title.set_text("FFT de l'image")
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(fshift_mask_mag, cmap='gray')
ax3.title.set_text("FFT + Masque r=96%")
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(img_retour, cmap='gray')
ax4.title.set_text("Aprés FFT inverse")
plt.show()
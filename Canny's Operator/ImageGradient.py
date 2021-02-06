import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('GaussianImages/Figure_6.png')

Sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)


sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

plt.imshow(sobel_8u,cmap='gray'),plt.title("Figure_6")
cv2.imwrite('ImageGradient/img21.png',sobel_8u)
plt.show()


# References
#  1. https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/filter_2d/filter_2d.html
#  2. https://www.meccanismocomplesso.org/en/opencv-python-edge-detection-and-image-gradient-analysis/
#  3.
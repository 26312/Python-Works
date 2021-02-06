import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('GrayScaledImages/image1.png')

gaussian_filter = cv2.GaussianBlur(img,(5,5),0)

plt.imshow(gaussian_filter),plt.title('Blurredimage1')

cv2.imwrite('GaussianImages/Bluredimage1.png',gaussian_filter)
plt.show()

### References

# 1. https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html
# 2. https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123
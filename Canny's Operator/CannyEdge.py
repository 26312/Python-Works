import cv2
import numpy as np
from matplotlib import pyplot as plt



img = cv2.imread('Images/img14.jpg',0)
edges = cv2.Canny(img,100,200)

title = ['image', 'canny']
images = [img, edges]

for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

cv2.imwrite('CannyImages/img23.png',edges)
plt.show()

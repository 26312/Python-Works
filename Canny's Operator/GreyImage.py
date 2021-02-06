# The following codes has been used to convert the images into gray scale
# Converting the images to Grayscale is the first step before moving towards Canny's Edge Operator
# In simple terms we can say that converting an image into a grey scale is a kind of pre-requisite to Canny's Edge Operator


import cv2  # The opencv-python package is imported using 'import cv2'

img_src = 'OilWaterScreenShots/SS9.png' # import the image from the src
                                        # had to be manually changed for every image

img = cv2.imread(img_src,0) # The function imread loads an image from the specified file and returns it. If the image cannot be
                            #.   read (because of missing file, improper permissions, unsupported or invalid format), the function
                            # .   returns an empty matrix ( Mat::data==NULL ).


cv2.imshow('image15',img) # 
#   The function imshow displays an image in the specified window. If the window was created with the
#   .   cv::WINDOW_AUTOSIZE flag, the image is shown with its original size, however it is still limited by the screen resolution.
#  .   Otherwise, the image is scaled to fit the window. The function may scale the image, depending on its depth:


cv2.imwrite('GrayScaledImages/image15.png',img)
#     The function imwrite saves the image to the specified file. The image format is chosen based on the
#     .   filename extension (see cv::imread for the list of extensions). In general, only 8-bit
#     .   single-channel or 3-channel (with 'BGR' channel order) images

cv2.waitKey(0)
cv2.destroyAllWindows()

### References
# 1. https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123
# 2. https://www.science-emergence.com/Articles/How-to-convert-an-image-to-grayscale-using-python-/
# 3. https://www.youtube.com/watch?v=q9sY9w2tn5M

# Python program to compress image to 1/4 of its original size without losing quality and pixels

# importing OpenCV(cv2) module 
import cv2 

# Save image in set directory 
img = cv2.imread('Test_2.jpg') 

# save image with lower compression—bigger file size and high resolution but faster decoding
cv2.imwrite('Test_2_comp.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])



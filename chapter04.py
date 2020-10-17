import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# print(img) # Print pixel value

# img[:] = 255, 0, 0 # Change pixel color

# cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3)  # Draw line
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)  # Draw line

cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)  # Draw rectangle
# cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)  # Draw rectangle with filled color

cv2.circle(img, (400, 50), 30, (255, 255, 0), 2)  # Draw circle

cv2.putText(img, 'OpenCV Self Learning', (50, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 2)

cv2.imshow('Image', img)
cv2.waitKey(0)

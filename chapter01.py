import cv2

print("Package imported")

# Image read
img = cv2.imread('Resources/lena.png')
cv2.imshow('OutPut', img)
#cv2.waitKey(0) #wait for infinity time
cv2.waitKey(2000) #wait for 2 seconds

# Video read
cap = cv2.VideoCapture('Resources/sample_video.mp4')
while True:
    success, img = cap.read()
    cv2.imshow('Video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Camera read
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100) #Set Brightness

while True:
    success, img = cap.read()
    cv2.imshow('Video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
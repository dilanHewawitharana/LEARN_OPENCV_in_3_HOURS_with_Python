import cv2
import numpy as np


def val_changed(val):
    update_val()


def update_val():
    global h_min, s_min, v_min, h_max, s_max, v_max
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBars')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBars')
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBars')
    s_max = cv2.getTrackbarPos('Sat Max', 'TrackBars')
    v_min = cv2.getTrackbarPos('Val Min', 'TrackBars')
    v_max = cv2.getTrackbarPos('Val Max', 'TrackBars')


def stack_images(scale, img_array):
    rows = len(img_array)
    cols = len(img_array[0])
    rows_available = isinstance(img_array[0], list)
    width = img_array[0][0].shape[1]
    height = img_array[0][0].shape[0]
    if rows_available:
        for x in range(0, rows):
            for y in range(0, cols):
                if img_array[x][y].shape[:2] == img_array[0][0].shape[:2]:
                    img_array[x][y] = cv2.resize(img_array[x][y], (0, 0), None, scale, scale)
                else:
                    img_array[x][y] = cv2.resize(img_array[x][y], (img_array[0][0].shape[1], img_array[0][0].shape[0]),
                                                 None, scale, scale)
                if len(img_array[x][y].shape) == 2: img_array[x][y] = cv2.cvtColor(img_array[x][y], cv2.COLOR_GRAY2BGR)
        image_blank = np.zeros((height, width, 3), np.uint8)
        hor = [image_blank] * rows
        hor_con = [image_blank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(img_array[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if img_array[x].shape[:2] == img_array[0].shape[:2]:
                img_array[x] = cv2.resize(img_array[x], (0, 0), None, scale, scale)
            else:
                img_array[x] = cv2.resize(img_array[x], (img_array[0].shape[1], img_array[0].shape[0]), None, scale,
                                          scale)
            if len(img_array[x].shape) == 2: img_array[x] = cv2.cvtColor(img_array[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(img_array)
        ver = hor
    return ver


def show_images():
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    img_result = cv2.bitwise_and(img, img, mask=mask)

    img_stack = stack_images(0.6, ([img, imgHSV], [mask, img_result]))
    cv2.imshow('Stacked Image', img_stack)


cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 310)
cv2.createTrackbar('Hue Min', 'TrackBars', 0, 179, val_changed)
cv2.createTrackbar('Sat Min', 'TrackBars', 0, 255, val_changed)
cv2.createTrackbar('Val Min', 'TrackBars', 0, 255, val_changed)

cv2.createTrackbar('Hue Max', 'TrackBars', 179, 179, val_changed)
cv2.createTrackbar('Sat Max', 'TrackBars', 255, 255, val_changed)
cv2.createTrackbar('Val Max', 'TrackBars', 255, 255, val_changed)

# Camera read
cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)  # Set Brightness

img = np.zeros((640, 480, 3), np.uint8)
imgHSV = np.zeros((640, 480, 3), np.uint8)

h_min = s_min = v_min = 0
h_max = s_max = v_max = 255

while True:
    success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    update_val()

    show_images()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

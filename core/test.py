import cv2
import numpy as np
import pyautogui
import time


# -------------------------------------------------
def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('Jump')
    pyautogui.keyUp('space')


# -------------------------------------------------
def pressLeft():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('Jump')
    pyautogui.keyUp('left')


# ---------------------------------------------------
def pressRight():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('Jump')
    pyautogui.keyUp('right')


# ---------------------------------------------------
def pressDown():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('Jump')
    pyautogui.keyUp('down')


# ---------------------------------------------------


lower_pink = np.array([170, 50, 50])
upper_pink = np.array([180, 255, 255])
threshold = 100  # TODO Adapt to your needs.
cap = cv2.VideoCapture(0)
while True:

    _, frame = cap.read()
    _, frame1 = cap.read()
    cv2.rectangle(frame, (100, 100), (400, 400), (0, 255, 0), 0)
    frame = frame[80:150, 0:1080]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_pink, upper_pink)
    mask1 = cv2.inRange(hsv1, lower_pink, upper_pink)
    cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    cv2.imshow('frame1', frame1)
    cv2.imshow('mask1', mask1)
    if cv2.countNonZero(mask) > threshold and cv2.countNonZero(mask1) > threshold:
        print('FOUND')
        pressSpace()
        time.sleep(0.05)
    if cv2.waitKey(20) == 27:
        break

cv2.destroyAllWindows()

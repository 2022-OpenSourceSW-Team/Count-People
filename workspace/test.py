import numpy as np
import cv2
from tkinter import *
import os
import time

# setting up the haar cascade classifiers from the opencv installation
face_cascade = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../haarcascades/haarcascade_eye.xml')

webcam = cv2.VideoCapture(0)
if not webcam.isOpened():
    print("Could not open webcam")
    exit()

while webcam.isOpened():
    status, frame = webcam.read()
    # cv2.imshow("frame", frame)

    # img = cv2.imread('2.JPG')

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # search for faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # for each face, detect eyes
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

    # displaying the image
    cv2.imshow('img', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
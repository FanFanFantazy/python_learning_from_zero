# coding=utf-8
# 性别识别

import cv2
from keras.models import load_model
import numpy as np
face_classifier = cv2.CascadeClassifier(
    r"./openCv/opencv/data/haarcascades/haarcascade_frontalface_default.xml")
gender_classifier = load_model("genderModel.hdf5")
gender_labels = {0: 'Female', 1: 'Male'}


def detectFace(img):
    # img = cv2.imread("test2.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,
                                             scaleFactor=1.2,
                                             minNeighbors=3,
                                             minSize=(70, 70))
    
    color = (115, 233, 86)

    for (x, y, w, h) in faces:
        face = img[(y - 60):(y + h + 60), (x - 30):(x + w + 30)]
        face = cv2.resize(face, (48, 48))
        face = np.expand_dims(face, 0)
        face = face / 255.0
        gender_label_arg = np.argmax(gender_classifier.predict(face))
        gender = gender_labels[gender_label_arg]
        cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)
        cv2.putText(img, gender, (x, y + 1), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    color, 2)
    cv2.imshow("Image", img)


cap = cv2.VideoCapture(0)
while (1):  # 逐帧显示
    ret, img = cap.read()
    # cv2.imshow("Image", img)
    try:
        detectFace(img)
    except BaseException:
        continue
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()  # 释放摄像头
cv2.waitKey()
cv2.destroyAllWindows()  # 释放窗口资源

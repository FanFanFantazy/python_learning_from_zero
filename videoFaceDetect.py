# coding=utf-8

import cv2
faceClassifier = cv2.CascadeClassifier(
    r"./openCv/opencv/data/haarcascades/haarcascade_frontalface_default.xml")
eyesClassifier = cv2.CascadeClassifier(
    r"./openCv/opencv/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml"
)

colorSet = [(0, 191, 255), (255, 191, 0)]  # 定义矩形颜色 - DeepSkyBlue1


def detectFace(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faceRects = faceClassifier.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=3, minSize=(80, 80))

    eyesRects = eyesClassifier.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=3, minSize=(15, 15))

    for faceRect in faceRects:  # 框出每一张人脸
        x, y, w, h = faceRect
        # 框出人脸
        cv2.rectangle(img, (x, y), (x + h, y + w), colorSet[0], 2)

    for eyesRect in eyesRects:  # 框出每一只眼睛
        x, y, w, h = eyesRect
        # 框出眼睛
        cv2.rectangle(img, (x, y), (x + h, y + w), colorSet[1], 2)
    cv2.imshow("Image", img)


cap = cv2.VideoCapture(0)
while (1):  # 逐帧显示
    ret, img = cap.read()
    try:
        detectFace(img)
    except BaseException:
        continue
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()  # 释放摄像头
cv2.destroyAllWindows()  # 释放窗口资源

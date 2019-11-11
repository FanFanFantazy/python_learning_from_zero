import cv2

filepath = "test2.jpg"
img = cv2.imread(filepath)  # 读取图片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换灰色

# OpenCV人脸识别分类器 括号中内容为识别器脚本的地址
faceClassifier = cv2.CascadeClassifier(
    r"./openCv/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
)

eyesClassifier = cv2.CascadeClassifier(
    r"./openCv/opencv/data/haarcascades/haarcascade_eye.xml"
)

colorSet = [(0, 191, 255), (255, 191, 0)]  # 定义矩形颜色 - DeepSkyBlue1
# 调用openCv人脸试别模块
faceRects = faceClassifier.detectMultiScale(
    gray, scaleFactor=1.2, minNeighbors=3, minSize=(70, 70))

eyesRects = eyesClassifier.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=3, minSize=(15, 15))

if len(faceRects) and len(eyesRects):  # 大于0
    for faceRect in faceRects:  # 框出每一张人脸
        x, y, w, h = faceRect
        # 框出人脸
        cv2.rectangle(img, (x, y), (x + h, y + w), colorSet[0], 2)

    for eyesRect in eyesRects:  # 框出每一只眼睛
        x, y, w, h = eyesRect
        # 框出眼睛
        cv2.rectangle(img, (x, y), (x + h, y + w), colorSet[1], 2)

cv2.imshow("image", img)  # 显示图像

cv2.waitKey(0)
cv2.destroyAllWindows()

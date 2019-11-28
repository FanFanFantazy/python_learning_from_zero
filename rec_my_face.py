import cv2
import os
from face_train import Model

path_name = './faceData/'


def recFace():
    # 加载模型
    counter = 0
    for dir_item in os.listdir(path_name):
        counter += 1
        if dir_item.endswith('.face.model.h5'):
            model = Model()
            model.load_model(file_path=path_name + dir_item)
            # 框住人脸的矩形边框颜色
            color = (0, 255, 0)
            # 捕获指定摄像头的实时视频流
            cap = cv2.VideoCapture(0)
            # 循环检测识别人脸
            while True:
                try:
                    ret, frame = cap.read()   # 读取一帧视频
                    # 图像灰化，降低计算复杂度
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    # 使用人脸识别分类器，读入分类器
                    cascade = cv2.CascadeClassifier(
                        r"./openCv/opencv/data/haarcascades/" +
                        "haarcascade_frontalface_default.xml"
                    )
                    # 利用分类器识别出哪个区域为人脸
                    faceRects = cascade.detectMultiScale(
                        frame_gray, scaleFactor=1.2, minNeighbors=3, minSize=(
                            70, 70
                        )
                    )
                    for (x, y, w, h) in faceRects:
                        # 截取脸部图像提交给模型识别这是谁
                        image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                        faceID = model.face_predict(image)
                        print(faceID)
                        cv2.rectangle(frame, (x, y), (x + h, y + w), color, 2)
                        # 如果是“我”
                        if faceID == 0:
                            # 文字提示是谁
                            cv2.putText(
                                frame, dir_item.split('.')[0], (
                                    x, y + 1
                                ), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (
                                    115, 233, 86
                                ), 2
                            )
                        else:
                            pass
                    cv2.imshow("Detect my face", frame)
                    # 等待10毫秒看是否有按键输入
                    k = cv2.waitKey(10)
                    # 如果输入q则退出循环
                    if k & 0xFF == ord('q'):
                        break
                except BaseException:
                    continue
            # 释放摄像头并销毁所有窗口
            cap.release()
            cv2.destroyAllWindows()
            break
        elif counter == len(os.listdir(path_name)):
            print('No model has been found, please craft a model first!')
            break


if __name__ == '__main__':
    recFace()

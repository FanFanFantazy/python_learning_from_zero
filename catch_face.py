import cv2


def CatchFace(window_name, catch_pic_num, path_name):
    cv2.namedWindow(window_name)
    cap = cv2.VideoCapture(0)
    classfier = cv2.CascadeClassifier(
        r"./openCv/opencv/data/haarcascades/haarcascade_frontalface_alt2.xml"
    )
    color = (115, 233, 86)
    num = 1
    while cap.isOpened():
        try:
            ok, frame = cap.read()
            grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faceRects = classfier.detectMultiScale(
                grey, scaleFactor=1.2, minNeighbors=3, minSize=(80, 80)
            )
            if len(faceRects) > 0:
                for (x, y, w, h) in faceRects:
                    img_name = '%s/%d.jpg' % (path_name, num)  # 定义图片存储路径+图片名称
                    image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                    cv2.imwrite(img_name, image)  # 将当前帧保存为图片
                    num += 1
                    if num > (catch_pic_num):   # 成功捕捉超过1000次突出循环
                        break
                    cv2.rectangle(
                        frame, (x - 10, y - 10), (
                            x + w + 10, y + h + 10
                        ), color, 2
                    )  # 画矩形
                    cv2.putText(
                        frame, 'num:%d' % (num), (
                            x + 30, y + 30
                        ), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 4
                    )  # 显示当前捕捉人脸图片是第几个
            # 超过指定最大保存数量结束程序
            if num > (catch_pic_num):
                break
            cv2.imshow(window_name, frame)
            c = cv2.waitKey(10)
            if c & 0xFF == ord('q'):
                break
        except BaseException:
            continue
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    CatchFace("CatchFace", 1000, './faceData/posFaceData')

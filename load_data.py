import os
import numpy as np
import cv2

IMAGE_SIZE = 64  # 定义缩放图片大小为64*64


# 缩放图片
def resize_image(image, height=IMAGE_SIZE, width=IMAGE_SIZE):
    top, bottom, left, right = (0, 0, 0, 0)
    # 获取图像尺寸
    h, w, _ = image.shape
    # 对于长宽不相等的图片，找到最长的一边
    longest_edge = max(h, w)
    # 短边需要增加像素使其与长边相等
    if h < longest_edge:
        dh = longest_edge - h
        top = dh // 2
        bottom = dh - top
    elif w < longest_edge:
        dw = longest_edge - w
        left = dw // 2
        right = dw - left
    else:
        pass
    # 补充的地方颜色
    BLACK = [0, 0, 0]
    # 给图像增加左右、上下，cv2.BORDER_CONSTANT指定边界，颜色由value指定
    constant = cv2.copyMakeBorder(
        image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=BLACK
    )
    # 调整图像大小
    return cv2.resize(constant, (height, width))


# 读取训练数据
images = []
labels = []


def read_path(path_name):
    for dir_item in os.listdir(path_name):  # os.listdir返回指定的文件夹包含的文件或文件夹的名字的列表
        # os.path.abspath，os.path.join 拼接输入路径和当前文件名
        full_path = os.path.abspath(os.path.join(path_name, dir_item))
        if os.path.isdir(full_path):  # 如果是文件夹，继续递归调用
            read_path(full_path)
        else:   # 文件
            if dir_item.endswith('.jpg'):
                image = cv2.imread(full_path)
                image = resize_image(image, IMAGE_SIZE, IMAGE_SIZE)
                images.append(image)  # 统计图片名
                labels.append(path_name)  # 统计文件名
    return images, labels


# 从指定路径读取训练数据
def load_dataset(path_name):
    images, labels = read_path(path_name)
    images = np.array(images)
    print(images.shape)
    # 标注数据，'posFaceData'文件夹下都是正向图片，全部为0，negFaceData下为反向图片，为1
    labels = np.array(
        [0 if label.endswith('posFaceData') else 1 for label in labels]
    )
    return images, labels


if __name__ == '__main__':
    images, labels = load_dataset("./faceData")

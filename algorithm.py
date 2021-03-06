from copy import copy
from math import log10, sqrt

import numpy as np
from cv2 import cv2


def sobel(img):
    """
    利用 sobel 算子 进行边缘检测
    读入 OpenCV格式的BGR图像，返回OpenCV格式的灰度图像
    """

    # 定义sobel算子
    sobel_x = [[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]]
    sobel_y = [[-1, -2, 1],
               [0, 0, 0],
               [1, 2, -1]]
    # 定义阈值
    valve = 116
    # 转换为灰度图
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 获取长宽
    row, col = img_gray.shape
    result = np.zeros((row, col))
    for x in range(1, row-1):
        for y in range(1, col-1):
            # 不管四个边进行边缘检测
            sub = img_gray[x-1:x+2, y-1:y+2]
            var_x = np.sum(sub*sobel_x)
            var_y = np.sum(sub*sobel_y)
            var = abs(var_x) + abs(var_y)
            if(var > valve):
                var = 0
            else:
                var = 255
            result[x, y] = var
    return result


def prewitt(img):
    """
    利用 prewitt 算子进行边缘检测
    读入 OpenCV格式的BGR图像，返回OpenCV格式的灰度图像
    """
    # 定义prewitt算子
    prewittx = [[-1, 0, 1],
                [-1, 0, 1],
                [-1, 0, 1]]
    prewitty = [[1, 1, 1],
                [0, 0, 0],
                [-1, -1, -1]]
    prewittx = np.array(prewittx)
    prewitty = np.array(prewitty)
    # 定义阈值
    valve = 116
    # 转换为灰度图
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 获取长宽
    row, col = img_gray.shape
    result = np.zeros((row, col))
    for x in range(1, row-1):
        for y in range(1, col-1):
            # 不管四个边进行边缘检测
            sub = img_gray[x-1:x+2, y-1:y+2]
            var_x = np.sum(sub*prewittx)
            var_y = np.sum(sub*prewitty)
            var = sqrt(var_x*var_x+var_y*var_y)
            if(var > valve):
                var = 0
            else:
                var = 255
            result[x, y] = var

    return result


def laplace(img):
    """
    利用拉普拉斯算子进行边缘检测
    读入 OpenCV格式的BGR图像，返回OpenCV格式的灰度图像
    """
    # 定义 laplace 算子
    laplaceop = [[0, 1, 0],
                 [1, -4, 1],
                 [0, 1, 0]]
    laplaceop = np.array(laplaceop)
    # 定义阈值
    valve = 40
    # 转换为灰度图
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 获取长宽
    row, col = img_gray.shape
    result = np.zeros((row, col))
    for x in range(1, row-1):
        for y in range(1, col-1):
            # 不管四个边进行边缘检测
            sub = img_gray[x-1:x+2, y-1:y+2]
            var = np.sum(sub*laplaceop)
            if(var > valve):
                var = 0
            else:
                var = 255
            result[x, y] = var
    return result


def log(img):
    """
    利用 log 算子 边缘检测
    输入OpenCV格式的BGR图片，输出OpenCV格式的灰度图
    """
    # 定义 LOG 算子
    logop = [[-2, -4, -4, -4, -2],
             [-4, 0, 8, 0, -4],
             [-4, 8, 24, 8, -4],
             [-4, 0, 8, 0, -4],
             [-2, -4, -4, -4, -2]]
    logop = np.array(logop)
    # 定义阈值
    valve = 116
    # 转换为灰度图
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 获取长宽
    row, col = img_gray.shape
    result = np.zeros((row, col))
    for x in range(2, row-2):
        for y in range(2, col-2):
            # 不管四个边进行边缘检测
            sub = img_gray[x-2:x+3, y-2:y+3]
            var = np.sum(sub*logop)
            if(var > valve):
                var = 0
            else:
                var = 255
            result[x, y] = var
    return result


def logwithzero(img):
    """
    log算法 有零交叉 边缘检测
    输入OpenCV格式的BGR图片，输出OpenCV格式的灰度图
    """
    # 定义 LOG 算子
    logop = [[-2, -4, -4, -4, -2],
             [-4, 0, 8, 0, -4],
             [-4, 8, 24, 8, -4],
             [-4, 0, 8, 0, -4],
             [-2, -4, -4, -4, -2]]
    logop = np.array(logop)
    # 定义阈值
    value = 116
    # 转换为灰度图
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 获取长宽
    row, col = img_gray.shape
    result = np.zeros((row, col))

    def isZeroCross(img, x, y):
        """
        判断该点是否是零交叉点，如果是则返回 True ;不是则返回 False
        
        以p为中心的一个3*3领域，p点处的零交叉意味着
        1. 至少有两个相对的领域像素的符号不同。
        在这个基础上还要判断中心点p的值介于两个符号不同像素的值之间，就是
        2. p的值要小于两个符号不同的像素的绝对值。
        如果是，那才可以判断为零交叉点
        """
        # flag表示这是不是零交叉点
        flag = False

        def diff(a, b):
            """
                如果a,b异号则返回True，其余情况返回False
            """
            if (a > 0) and (b < 0):
                return True
            elif (a < 0) and (b > 0):
                return True
            return False

        def abssmall(a, b):
            """"
            如果a的绝对值小于b的绝对值则返回True，其余情况返回False
            """
            if(abs(a) < abs(b)):
                return True
            else:
                return False
        # 判断是不是零交叉点
        if abssmall(img[x][y], img[x-1][y]) and abssmall(img[x][y], img[x+1][y]) and diff(img[x-1][y], img[x+1][y]):
            flag = True
        elif abssmall(img[x][y], img[x-1][y-1]) and abssmall(img[x][y], img[x+1][y+1]) and diff(img[x-1][y-1], img[x+1][y+1]):
            flag = True
        elif abssmall(img[x][y], img[x][y-1]) and abssmall(img[x][y], img[x][y+1]) and diff(img[x][y-1], img[x][y+1]):
            flag = True
        elif abssmall(img[x][y], img[x-1][y+1]) and abssmall(img[x][y], img[x+1][y-1]) and diff(img[x-1][y+1], img[x+1][y-1]):
            flag = True
        return flag

    count = 0
    for x in range(2, row-2):
        for y in range(2, col-2):
            # 不管四个边进行边缘检测
            sub = img_gray[x-2:x+3, y-2:y+3]
            var = np.sum(sub*logop)
            result[x, y] = var
            if var > value :
                count += 1
    print("无零交叉信噪比是:{0}%".format(100*count/(row*col-count)))

    count = 0
    tmpImg = copy(result)
    for x in range(1, row-1):
        for y in range(1, col-1):
            if (isZeroCross(result, x, y) and result[x][y] > value):
                var = 0
                count += 1
            else:
                var = 255
            tmpImg[x][y] = var
    print("有零交叉信噪比是:{0}%".format(100*count/(row*col-count)))
    result = tmpImg
    return result


def genrate(img):
    """
    迭代阈值法
    输入OpenCV格式的BGR图，输出OpenCV格式的灰度图
    """
    # 转换为灰度图
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 获取长宽
    row, col = img_gray.shape
    result = np.zeros((row, col))
    # 求第一代阈值
    value = int((int(img_gray.max()) + int(img_gray.min()))/2)
    # 生成直方图便于计算
    F = np.zeros(256)
    for x in range(row):
        for y in range(col):
            F[img_gray[x][y]] = F[img_gray[x][y]] + 1
    # 获得前景色的数量

    def getFrontColorNum(median):
        nFrontColor = 0
        for i in range(median, 256):
            nFrontColor = nFrontColor + F[i]
        return nFrontColor

    # 获得背景色的数量
    def getBackColorNum(median):
        nBackColor = 0
        for i in range(median):
            nBackColor = nBackColor + F[i]
        return nBackColor

    # 计算下一代阈值
    def getNextValue(median):
        tmp1 = 0
        tmp2 = 0
        sum1 = 0
        sum2 = 0
        for i in range(median, 256):
            tmp1 = tmp1 + F[i] * i
        sum1 = tmp1/getFrontColorNum(median)
        for i in range(median):
            tmp2 = tmp2 + F[i] * i
        sum2 = tmp2/getBackColorNum(median)
        return (sum1+sum2)/2

    nextValue = int(getNextValue(value))
    # 迭代阈值
    while (nextValue != value):
        value = nextValue
        nextValue = int(getNextValue(value))

    value = int(value)
    print("迭代阈值法的结果为", value)
    # 二值化
    for x in range(row):
        for y in range(col):
            if value > img_gray[x][y]:
                result[x][y] = 0
            else:
                result[x][y] = 255
    return result


def maximus(img):
    """
    一维最大熵
    输入OpenCV格式的BGR图片，输出OpenCV格式的灰度图
    Threshold 阈值
    参考 https://blog.csdn.net/Robin__Chou/article/details/53931442
    """
    # 转换为灰度图
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 获取长宽
    row, col = img_gray.shape
    # 生成结果图像矩阵
    result = np.zeros((row, col))
    # 生成直方图便于计算
    F = np.zeros(256)
    for x in range(row):
        for y in range(col):
            F[img_gray[x][y]] = F[img_gray[x][y]] + 1

    def getFrontColorNum(median):
        """获得前景色的数量，输入 median 为阈值的大小"""
        nFrontColor = 0
        for i in range(median, 256):
            nFrontColor = nFrontColor + F[i]
        return nFrontColor

    def getBackColorNum(median):
        """获得背景色的数量，输入 median 为阈值的大小"""
        nBackColor = 0
        for i in range(median):
            nBackColor = nBackColor + F[i]
        return nBackColor

    maxEntropy = -10
    threshold = 0
    # 求出最大熵
    for tmpThreshold in range(256):
        nFrontColor = getFrontColorNum(tmpThreshold)
        nBackColor = getBackColorNum(tmpThreshold)
        # 计算背景熵
        backEntropy = 0
        for i in range(tmpThreshold):
            if F[i] != 0:
                Property = F[i]/nBackColor
                backEntropy = -Property*log10(float(Property)) + backEntropy
        # 计算前景熵
        frontEntropy = 0
        for i in range(tmpThreshold, 256):
            if F[i] != 0:
                Property = F[i]/nFrontColor
                frontEntropy = -Property*log10(float(Property)) + frontEntropy
        # 求最大熵
        if (frontEntropy + backEntropy >= maxEntropy):
            maxEntropy = frontEntropy + backEntropy
            threshold = tmpThreshold
    print("一维最大熵的阈值为：", threshold)
    # 二值化结果
    for x in range(row):
        for y in range(col):
            if threshold > img_gray[x][y]:
                result[x][y] = 0
            else:
                result[x][y] = 255
    return result


if __name__ == "__main__":
    imgpath = "lena.jpg"
    img = cv2.imread(imgpath)
    img = laplace(img)
    cv2.imshow("s", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

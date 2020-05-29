from cv2 import cv2
import numpy as np

# 读入 OpenCV格式的BGR图像，返回OpenCV格式的图像
def sobel (img):
    # 定义sobel算子
    sobel_x = [[-1,0,1],
            [-2,0,2],
            [-1,0,1]]
    sobel_y = [[-1,-2,1],
            [0,0,0],
            [1,2,-1]]
    # 定义阈值
    valve = 188
    # 转换为灰度图
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   
    # 获取长宽 
    rol,cow = img_gray.shape
    result = np.zeros((rol,cow))
    for x in range(1,rol-1):
        for y in range(1,cow-1):
            # 不管四个边进行边缘检测
            sub = img_gray[x-1:x+2,y-1:y+2]
            var_x = np.sum(np.matmul(sub,sobel_x))
            var_y = np.sum(np.matmul(sub,sobel_y))
            var = abs(var_x) + abs(var_y)
            if(var > valve):
                var = 0
            else :
                var = 255
            result[x,y] = var
    return result

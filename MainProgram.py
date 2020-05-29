import sys

import inspect


from cv2 import cv2 
from PyQt5 import QtGui
from PyQt5.Qt import QPixmap 
from PyQt5.QtWidgets import (QApplication, QFileDialog, QGraphicsScene,
                             QMainWindow)

from MainWindow import *


class MyWindow(QMainWindow, Ui_MainWindow):
    # 初始化
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        # 注册监听
        self.actionOpen_File.triggered.connect(self.openfile)
        self.actionStorage_File.triggered.connect(self.savefile)

        self.action_sobel.triggered.connect(self.sobelWork)
        self.action_priwitt.triggered.connect(self.priwittWOrk)
        self.action_laplace.triggered.connect(self.laplaceWork)

        self.action_genrate.triggered.connect(self.genrateWork)
        self.action_LOG.triggered.connect(self.logWork)
        self.action_maximus.triggered.connect(self.maximusWork)
        # 初始化实例变量
        self.srcImg =[]    # 原始图像，储存为 OpenCV 中的图像格式
        self.destImg  =[]  # 原始图像，储存为 OpenCV 中的图像格式



    # 将用 opencv 读入的图像转换成qt可以读取的图像
    def cvPic2Qimg(self,img):
        print(img.shape)
        if(img.shape[2]==3):
            #转换为RGB排列
            RGBImg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            #RGBImg.shape[1]*RGBImg.shape[2]这一句时用来解决扭曲的问题
            #详情参考 https://blog.csdn.net/owen7500/article/details/50905659 这篇博客
            image=QtGui.QImage(RGBImg,RGBImg.shape[1],RGBImg.shape[0],
                                RGBImg.shape[1]*RGBImg.shape[2],QtGui.QImage.Format_RGB888)
        elif (img.shape[2] == 4):
            RGBImg=cv2.cvtColor(img,cv2.COLOR_BGRA2RGB)
        return image
    
    # 打开图片
    def openfile(self): 
        # 获得图片地址，图片类型
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        if imgType != "*.jpg" and imgType != "*.png":
            return 
        print(imgName,imgType)
        # 利用OpenCV读入图片并存入self.srcImg中
        self.srcImg = cv2.imread(imgName)
        # 将OpenCV格式储存的图片转换为QT可处理的图片类型
        qimg = self.cvPic2Qimg(self.srcImg)
        # 将图片放入图片显示窗口
        
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap.fromImage(qimg))
        self.picview_source.setScene(scene)
        # TODO: 增加自动调节大小适应窗口的功能

    # 保存图片
    def savefile(self):
        # 获得图片地址，图片类型
        imgName, imgType = QFileDialog.getSaveFileName(self, "保存图片", "*", "*.jpg;;*.png")
        print(imgName,imgType)

        # 利用OpenCV保存图片
        # 按不同的格式区分，分别对应不同的参数
        if imgType == "*.jpg" :
            cv2.imwrite(imgName,self.destImg, [cv2.IMWRITE_JPEG_QUALITY, 50])
        elif imgType == "*.png":
            cv2.imwrite(imgName,self.destImg, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    
    # 显示结果图像
    # 将self.destImg显示在 self.picview_result中
    def showResultPic(self):
        
        pass

    # 对原图像使用 sobel 算子卷积，并且将结果显示在处理图像栏
    def sobelWork(self) :
        print(inspect.stack()[0][3])
        pass    
    # 对原图像使用 priwitt 算子卷积，并且将结果显示在处理图像栏
    def priwittWOrk(self):
        print(inspect.stack()[0][3])
        pass
    # 对原图像使用 laplace 算子卷积，并且将结果显示在处理图像栏
    def laplaceWork(self):
        print(inspect.stack()[0][3])
        pass

    # 对原图像使用 迭代阈值法 边缘检测，并且将结果显示在处理图像栏
    def genrateWork(self):
        print(inspect.stack()[0][3])
        pass
    # 对原图像使用 log 算法边缘检测，并且将结果显示在处理图像栏
    def logWork(self):
        print(inspect.stack()[0][3])
        pass
    # 对原图像使用一维最大熵 算法边缘检测，并且将结果显示在处理图像栏
    def maximusWork(self):
        print(inspect.stack()[0][3])
        pass




        # self.action_genrate.triggered.connect(self.genrateWork)
        # self.action_LOG.triggered.connect(self.logWork)
        # self.action_maximus.triggered.connect(self.maximusWork)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())

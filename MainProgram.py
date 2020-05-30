import inspect
import sys
import threading
from qimage2ndarray import array2qimage
from cv2 import cv2
from PyQt5 import QtGui
from PyQt5.Qt import QPixmap
from PyQt5.QtGui import qRgb
from PyQt5.QtWidgets import (QApplication, QFileDialog, QGraphicsScene,
                             QMainWindow)

from MainWindow import *
from algorithm import *

class MyWindow(QMainWindow, Ui_MainWindow):
    # 初始化
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        # 注册监听
        # 打开文件的项
        self.actionOpen_File.triggered.connect(self.openfile)
        self.actionStorage_File.triggered.connect(self.savefile)
        # 边缘检测的项
        self.action_sobel.triggered.connect(self.sobelWork)
        self.action_prewitt.triggered.connect(self.prewittWOrk)
        self.action_laplace.triggered.connect(self.laplaceWork)
        # 阈值处理的项
        self.action_genrate.triggered.connect(self.genrateWork)
        self.action_LOG.triggered.connect(self.logWork)
        self.action_maximus.triggered.connect(self.maximusWork)
        # 初始化实例变量
        self.srcImg = np.zeros((256,256))     # 原始图像，储存为 OpenCV 中的图像格式
        self.destImg = np.zeros((256,256))    # 原始图像，储存为 OpenCV 中的图像格式

    def cvPic2Qimg(self, img):
        """
        将用 opencv 读入的图像转换成qt可以读取的图像

        ========== =====================
        序号       支持类型
        ========== =================
                 1 灰度图 Gray
                 2 三通道的图 BGR顺序
                 3 四通道的图 BGRA顺序
        ========= ===================
        """
        print(img.shape,img.size)
        if (len(img.shape)==2):
            # 读入灰度图的时候
            image = array2qimage(img)
        elif (len(img.shape)==3):  
            # 读入RGB或RGBA的时候
            if (img.shape[2] == 3):
                #转换为RGB排列
                RGBImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                #RGBImg.shape[1]*RGBImg.shape[2]这一句时用来解决扭曲的问题
                #详情参考 https://blog.csdn.net/owen7500/article/details/50905659 这篇博客
                image = QtGui.QImage(RGBImg, RGBImg.shape[1], RGBImg.shape[0],
                                    RGBImg.shape[1]*RGBImg.shape[2], QtGui.QImage.Format_RGB888)
            elif (img.shape[2] == 4):
                #读入为RGBA的时候
                RGBAImg = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
                image = array2qimage(RGBAImg)
        return image

    def openfile(self):
        """ 
        打开图片，并且保存在self.srcImg中
        """
        # 获得图片地址，图片类型
        imgName, imgType = QFileDialog.getOpenFileName(
            self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        if imgType != "*.jpg" and imgType != "*.png":
            return
        print(imgName, imgType)
        # 利用OpenCV读入图片并存入self.srcImg中
        self.srcImg = cv2.imread(imgName)
        # 缩放图像为适应窗口的大小
        # 获得缩放比例
        width = self.picview_source.width()
        height = self.picview_source.height()
        row,col = self.srcImg.shape[1],self.srcImg.shape[0]
        a = float(width/row)
        b = float(height/col)
        if a < b :
            scale = a
        else :
            scale = b
        dim = (int(row*scale),int(col*scale))
        # 缩放图像
        tmpImg = cv2.resize(self.srcImg,dim)
        # 将OpenCV格式储存的图片转换为QT可处理的图片类型
        qimg = self.cvPic2Qimg(tmpImg)
        # 将图片放入图片显示窗口
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap.fromImage(qimg))
        self.picview_source.setScene(scene)
        print(self.picview_source.size())

    def savefile(self):
        """
        保存处理结果的图片
        """
        if  self.srcImg.any() == self.destImg.any() :
            print("请先进行处理图像")
            return 
        # 获得图片地址，图片类型
        imgName, imgType = QFileDialog.getSaveFileName(
            self, "保存图片", "*", "*.jpg;;*.png")
        print(imgName, imgType)
        if (self.destImg==[]):
            print("没有处理结果！不进行保存")
            return 
        # 利用OpenCV保存图片
        # 按不同的格式区分，分别对应不同的参数
        if imgType == "*.jpg":
            cv2.imwrite(imgName, self.destImg, [cv2.IMWRITE_JPEG_QUALITY, 50])
        elif imgType == "*.png":
            cv2.imwrite(imgName, self.destImg, [cv2.IMWRITE_PNG_COMPRESSION, 0])

    def showResultPic(self):
        """
            显示结果图像,将self.destImg显示在 self.picview_result中 
        """
        # 缩放图像为适应窗口的大小
        # 获得缩放比例
        width = self.picview_result.width()
        height = self.picview_result.height()
        row,col = self.destImg.shape[1],self.destImg.shape[0]
        a = float(width/row)
        b = float(height/col)
        if a < b :
            scale = a
        else :
            scale = b
        dim = (int(row*scale),int(col*scale))
        # 缩放图像
        tmpImg = cv2.resize(self.destImg,dim)
        # 将OpenCV格式储存的图片转换为QT可处理的图片类型
        qimg = self.cvPic2Qimg(tmpImg)
        # 将图片放入图片显示窗口
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap.fromImage(qimg))
        self.picview_result.setScene(scene)     

    def sobelWork(self):
        """
            对原图像使用 sobel 算子卷积，并且将结果显示在处理图像栏
        """
        print(inspect.stack()[0][3])
        if  self.srcImg.any() == self.destImg.any() :
            print("请先打开图像！")
            return 
        self.destImg = sobel(self.srcImg)
        self.showResultPic()

    def prewittWOrk(self):
        """
        对原图像使用 prewitt 算子卷积，并且将结果显示在处理图像栏
        """
        print(inspect.stack()[0][3])
        if  self.srcImg.any() == self.destImg.any() :
            print("请先打开图像！")
            return 
        self.destImg = prewitt(self.srcImg)
        self.showResultPic()

    def laplaceWork(self):
        """
        对原图像使用 laplace 算子卷积，并且将结果显示在处理图像栏
        """
        print(inspect.stack()[0][3])
        if  self.srcImg.any() == self.destImg.any() :
            print("请先打开图像！")
            return 
        self.destImg = laplace(self.srcImg)
        self.showResultPic()
        pass
    
    def genrateWork(self):
        """
        对原图像使用 迭代阈值法 阈值检测 ，并且将结果显示在处理图像栏
        """
        print(inspect.stack()[0][3])
        if  self.srcImg.any() == self.destImg.any() :
            print("请先打开图像！")
            return 
        self.destImg = genrate(self.srcImg)
        self.showResultPic()
        pass

    def logWork(self):
        """
        对原图像使用 log 算法 阈值检测，并且将结果显示在处理图像栏
        """
        print(inspect.stack()[0][3])
        if  self.srcImg.any() == self.destImg.any() :
            print("请先打开图像！")
            return 
        self.destImg=log(self.srcImg)
        self.showResultPic()
        pass

    def maximusWork(self):
        """
        对原图像使用一维最大熵 算法 阈值检测 ，并且将结果显示在处理图像栏
        """
        print(inspect.stack()[0][3])
        if  self.srcImg.any() == self.destImg.any() :
            print("请先打开图像！")
            return 
        self.destImg = maximus(self.srcImg)
        self.showResultPic()
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())

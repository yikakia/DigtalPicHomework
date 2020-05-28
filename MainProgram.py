import sys
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QGraphicsScene
from MainWindow import *
from cv2 import cv2 as cv2

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionOpen_File.triggered.connect(self.openfile)

    # 将用opencv读入的图像转换成qt可以读取的图像
    def cvPic2Qimg(self,img):
        RGBImg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        image=QtGui.QImage(RGBImg,RGBImg.shape[1],RGBImg.shape[0],QtGui.QImage.Format_RGB888)
        return image
    
    # 将qimg转换为opencv可以处理的图像
    def openfile(self): 
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        if imgType != "*.jpg" and imgType != "*.png":
            return 
        print(imgName,imgType)
        img = cv2.imread(imgName)
        qimg = self.cvPic2Qimg(img)
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap.fromImage(qimg))
        self.picview_source.setScene(scene)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
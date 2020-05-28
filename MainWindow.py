# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 541))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 100, 801, 441))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.picview_source = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.picview_source.setObjectName("picview_source")
        self.horizontalLayout_3.addWidget(self.picview_source)
        self.picview_target = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.picview_target.setObjectName("picview_target")
        self.horizontalLayout_3.addWidget(self.picview_target)
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionss = QtWidgets.QAction(MainWindow)
        self.actionss.setObjectName("actionss")
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setCheckable(False)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionStorage_File = QtWidgets.QAction(MainWindow)
        self.actionStorage_File.setObjectName("actionStorage_File")
        self.menu.addAction(self.actionOpen_File)
        self.menu.addAction(self.actionStorage_File)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.actionOpen_File.triggered.connect(self.picview_source.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数字图像"))
        self.label.setText(_translate("MainWindow", "原始图像"))
        self.label_2.setText(_translate("MainWindow", "处理图像"))
        self.menu.setTitle(_translate("MainWindow", "文件(&F)"))
        self.actionss.setText(_translate("MainWindow", "ss"))
        self.actionOpen_File.setText(_translate("MainWindow", "打开文件(&O)"))
        self.actionOpen_File.setToolTip(_translate("MainWindow", "Ctrl+O"))
        self.actionStorage_File.setText(_translate("MainWindow", "储存文件(&S)"))
        self.actionStorage_File.setToolTip(_translate("MainWindow", "Ctrl+S"))

UI.ui文件是用于*QT designer*的文件

MainWindows.py文件是通过 *pyuic5.exe*转换`UI.ui`文件得到的.py程序

图像处理的函数统一在`algorithm.py`文件中，统一输入为OpenCV的MAT格式,BGR顺序，返回值为结果，格式为OpenCV的MAT格式,BGR顺序
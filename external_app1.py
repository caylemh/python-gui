import os
import time
import win32.win32gui as win32gui
import sys
import os
from PyQt5 import QtWidgets, QtGui
import subprocess


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout(widget)
        self.setCentralWidget(widget)

        exePath = "C:\\Windows\\system32\\calc.exe"
        # subprocess.Popen(exePath)
        os.system('"%s"' % exePath)
        hwnd = win32gui.FindWindow(0, 'Calculator')
        time.sleep(0.05)
        print(hwnd)
        self.window = QtGui.QWindow.fromWinId(hwnd)    
        self.windowcontainer = self.createWindowContainer(self.window, widget)

        layout.addWidget(self.windowcontainer, 0, 0)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    form = MainWindow()
    form.setWindowTitle('Embed')
    form.setGeometry(100, 100, 400, 600)
    form.show()
    sys.exit(app.exec_())


# Second Solution
# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()

#         widget = QtWidgets.QWidget()
#         layout = QtWidgets.QGridLayout(widget)
#         self.setCentralWidget(widget)

#         exePath = "C:\Windows\system32\calc.exe"
#         subprocess.Popen(exePath)
#         # os.system('"%s"' % exePath)
#         hwnd = win32gui.FindWindow(0, 'Calculator')
#         time.sleep(0.05)
#         window = QtGui.QWindow.fromWinId(hwnd)
#         self.createWindowContainer(window,self)
#         # self.setGeometry(500,500,450,400)
#         self.setWindowTitle("File Dialog")
#         self.show()

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     app.setStyle("fusion")
#     form = MainWindow()
#     form.setWindowTitle('My Embedded Calculator')
#     form.setGeometry(600, 600, 600, 600)
#     form.show()
#     sys.exit(app.exec_())

# Solution 3
# class MainWindow(QtWidgets.QMainWindow):

#     def __init__(self):
#         super(MainWindow, self).__init__()

#         # create a process
#         exePath = "C:\\Windows\\system32\\calc.exe"
#         subprocess.Popen(exePath)
#         # os.system(exePath)
#         hwnd = win32gui.FindWindow(0, 'Calculator')
#         print(hwnd)
#         time.sleep(0.05)
        
#         window = QtGui.QWindow.fromWinId(hwnd)
#         self.createWindowContainer(window, self)
#         self.setGeometry(0, 0, 502, 752)
#         # self.setWindowTitle('Embedded Window')
#         self.activateWindow()

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     form = MainWindow()
#     form.setWindowTitle(' Embedded ')
#     form.setGeometry(100, 100, 400, 600)
#     form.show()
#     sys.exit(app.exec_())

import win32.win32gui as win32gui
import subprocess
import os
import time
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget

# class ExWindow:
#   def initUI(self):
#       # create a process
#       exePath = "C:\\Windows\\system32\\calc.exe"
#       subprocess.Popen(exePath)
#       hwnd = win32gui.FindWindow(0,"Calculator")
#       print(hwnd)
#       time.sleep(0.05)
#       window = QtGui.QWindow.fromWinId(hwnd)
#       self.createWindowContainer(window, self)
#       self.setGeometry(500, 500, 450, 400)
#       self.setWindowTitle('File dialog')
#       self.show()

# w = ExWindow()
# w.initUI()

#-----------------------
# 1 - Create widget first
# 2 - Create function to open process
# 3 - Run the process inside the widget

#-----------------------


# 1
class MyWindow(QWidget):

  def __init__(self):
    super().__init__()

    self.initUI()
  
  def initUI(self):
    # create a process
    exePath = "C:\\Windows\\system32\\calc.exe"
    # subprocess.Popen(exePath)
    os.system(exePath)
    hwnd = win32gui.FindWindow(0,"Calculator")
    print(hwnd)
    time.sleep(0.05)
    window = QtGui.QWindow(screen=None)
    window.fromWinId(hwnd)
    self.createWindowContainer(window, self)
    self.setGeometry(100, 100, 600, 400)
    self.setWindowTitle('Embedded Program')
    self.show()

def main():

  app = QApplication(sys.argv)
  w = MyWindow()
  sys.exit(app.exec_())


if __name__ == '__main__':
  main()

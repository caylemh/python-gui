from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QLabel, QWidget
import sys
  
# proc = QtCore.QProcess()
# proc.start("ping", ["www.google.com", "-n", "5"])
# proc.waitForFinished()
# stdOut = proc.readAllStandardOutput()
# stdErr = proc.readAllStandardError()
  
# print ("Standard Out:")
# print (stdOut)
# print ("Standard Error:")
# print (stdErr)


# -- Hello World --
app = QApplication(sys.argv)
label = QLabel("Hello World!")
w = QWidget(label)
w.show()
app.exec_()
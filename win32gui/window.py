from tkinter import *
import os
import threading
import subprocess

# Solution 1
class Application(object):
    def __init__(self, root):
        super(Application, self).__init__()
        self.root = root

        self.main_container = Frame(self.root)#, bg="bisque")
        self.main_container.pack(side=TOP, fill="both", expand='yes')


        self.button_1 = Button(self.main_container, text = "Os", relief=RAISED, command = lambda: self.os_open())
        self.button_1.pack()
        self.button_2 = Button(self.main_container, text = "Subprocess", relief=RAISED, command = lambda: self.sub_open())
        self.button_2.pack()

    def os_open(self):
        os.system("c:\windows\system32\calc.exe")

    def sub_open(self):
        exe = "c:\windows\system32\calc.exe"
        process = subprocess.Popen(exe, stdout=subprocess.PIPE)
        process.wait()

# Solution 2
# class App:
#         def __init__(self, root):
#             self.frame = Frame(root)
#             self.b = Button(self.frame, text = 'Open', command = self.openFile)
#             self.b.grid(row = 1)
#             self.frame.grid()
#         def openFile(self):
#             os.startfile("c:\windows\system32\calc.exe")

root = Tk()
app = Application(root)
root.mainloop()
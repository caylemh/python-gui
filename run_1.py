import pygetwindow._pygetwindow_win as getwin
import os
import win32gui

# os.system("c:\windows\system32\calc.exe")
hwnd = win32gui.FindWindow(0, 'Calculator')
print(hwnd)
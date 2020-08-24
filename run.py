
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk

# Create instance
window = tk.Tk()   

# Add a title       
window.title("Python GUI")

# Add a Label

a_label = ttk.Label(window, text="A Label")
a_label.grid(column=0, row=0)

# Button click event

def click_me():
    action.configure(text="I have been clicked")
    a_label.configure(text='A Red Label')
    a_label.configure(foreground='red')

# Adding a button

action = ttk.Button(window, text="Click Here", command=click_me)
action.grid(column=0, row=1)


#======================
# Start GUI
#======================
window.mainloop()
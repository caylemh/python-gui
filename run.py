
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
    action.configure(text='Hello ' + name.get())

#Changing our label
ttk.Label(text="Enter a name: ").grid(column=0, row=0)

# Adding a Text box Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(window, width=12, textvariable=name)
name_entered.focus()  # Placing focus into the Entry box
name_entered.grid(column=0, row=1)

# Adding a button
action = ttk.Button(window, text="Click Here", command=click_me)
action.grid(column=1, row=1)
action.configure(state='disabled')


#======================
# Start GUI
#======================
window.mainloop()
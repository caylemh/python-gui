
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk, scrolledtext

# Create instance
window = tk.Tk()   

# Add a title       
window.title("Python GUI")

# Add a Label
a_label = ttk.Label(window, text="A Label")
a_label.grid(column=0, row=0)

# Button function
def click_me():
    action.configure(text='Hello ' + name.get() + ' ' + number_chosen.get())
    
#Changing our label
ttk.Label(text="Enter a name: ").grid(column=0, row=0)

# Adding a Text box Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(window, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

# Adding ComboBoxes
b_label = ttk.Label(window, text="Choose a number: ").grid(column=1, row=0)
number = tk.StringVar
number_chosen = ttk.Combobox(window, width=12, state='readonly', textvariable=number)
number_chosen['value'] = (1,2,3,42,100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

# Adding a button
action = ttk.Button(window, text="Click Here", command=click_me)
action.grid(column=2, row=1)
# action.configure(state='disabled')

# Adding Checkbuttons
chVarDis = tk.IntVar()
chVarUn = tk.IntVar()
chVarEn = tk.IntVar()

# Checkbox 1
check1 = tk.Checkbutton(window, text="Disabled", state='disabled', variable=chVarDis)
check1.select()
check1.grid(column=0, row=3, sticky=tk.W)

# Checkbox 2
check2 = tk.Checkbutton(window, text="Unchecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=3, sticky=tk.W)

# Checkbox 3
check3 = tk.Checkbutton(window, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=3, sticky=tk.W)

# Global Variables for Radio Buttons
colors = ['Blue', 'Gold', 'Red']

# Radio Button function
def radCall():
    radSel = radVar.get()
    if radSel == 0: window.configure(background=colors[0])
    elif radSel == 1: window.configure(background=colors[1])
    elif radSel == 2: window.configure(background=colors[2])

# Radio Buttons
radVar = tk.IntVar()
radVar.set(99)

for col in range(5):
    curRad = tk.Radiobutton(window, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=4, sticky=tk.W)

# rad1 = tk.Radiobutton(window, text="COLOR 1", variable=radVar, value=1, command=radCall)
# rad1.grid(column=0, row=4, sticky=tk.W, columnspan=3)
# rad2 = tk.Radiobutton(window, text="COLOR 2", variable=radVar, value=2, command=radCall)
# rad2.grid(column=1, row=4, sticky=tk.W, columnspan=3)
# rad3 = tk.Radiobutton(window, text="COLOR 3", variable=radVar, value=3, command=radCall)
# rad3.grid(column=2, row=4, sticky=tk.W, columnspan=3)

# ScrollText Widget
scrol_w = 50
scrol_h = 3

scroll = scrolledtext.ScrolledText(window, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scroll.grid(column=0, row=5, columnspan=3)

name_entered.focus()  # Placing focus into the Entry box

#======================
# Start GUI
#======================
window.mainloop()
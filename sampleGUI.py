import tkinter as tk
from tkinter import ttk
import time
win = tk.Tk()
win.title("Sample")
tabcontrol = ttk.Notebook(win)
tab1 = ttk.Frame(tabcontrol)
tabcontrol.add(tab1, text='Tab 1')
tab2 = ttk.Frame(tabcontrol)
tabcontrol.add(tab2, text='Tab2')
tabcontrol.pack(expand=1, fill='both')

frame1 = ttk.LabelFrame(tab1, text='Some Shite')
frame1.grid(row=0, column=0)

frame2 = ttk.LabelFrame(tab2, text='someother shite')
frame2.grid(row=1, column=0)

openButton = ttk.Button(frame1, text='Open Port', command=None)
openButton.grid(row=0, column=0, sticky='WE')
openButton.configure(state='DISABLED')

someotherbutton = ttk.Button(frame2, text='butt', command=None)
someotherbutton.grid(row=0, column=1, sticky='E')

def key_press(event):
    print(event.char, " pressed")
    print("time "+time.time())

frame1.bind("<Key>", key_press)

# main loop
win.mainloop()

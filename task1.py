from tkinter import*
import tkinter as tk

w = tk.Tk()
w.title('Task 1')
b1 = tk.Button(w, text='Button1').grid(row=0,column=1)
b2 = tk.Button(w, text='Button2').grid(row=1,column=0)
b3 = tk.Button(w, text='Button3').grid(row=1,column=2)
b4 = tk.Button(w, text='Button4').grid(row=2,column=1)
w.mainloop()
from tkinter import*
import tkinter as tk

def validate():
    
    e=e1.get()
    Label(master, text=e[::-1]).grid(row=2,column=1)
    
master = Tk()
master.title('Task 2')
Label(master, text='Enter a word:      ').grid(row=0)
b1 = tk.Button(master, text='Validate',command=validate).grid(row=3,column=1)
e1 = Entry(master)
e1.grid(row=0 , column=1)
master.mainloop()
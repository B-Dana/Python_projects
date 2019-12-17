import tkinter as tk
from tkinter import *
from tkinter import filedialog


root = Tk()
root.title('Choose directory')
root.geometry('{}x{}'.format(650,200))

dirName=StringVar()


btn = Button(root, text="Browse",width=10,height=1,font=('Times New Roman',13), command=lambda: askdirectory())
btn.grid(row=0, column=0, padx=(20,0), pady=(100,0))


txt = Text(root, height=1, width=55)
txt.grid(row=0,column=1, padx=(20,0), pady=(100,0))



def askdirectory():
    filepath=filedialog.askdirectory()
    dirName.set(filepath)
    txt.insert(END, dirName.get())
    


root.mainloop()




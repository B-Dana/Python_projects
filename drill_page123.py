import tkinter as tk
from tkinter import *
from tkinter import filedialog

import os
import shutil
import sqlite3



root = Tk()
root.title('Choose directory')
root.geometry('{}x{}'.format(670,250))

sourcePath=StringVar()
destPath=StringVar()


btn1 = Button(root, text="Source",width=10,height=1,font=('Times New Roman',13), command=lambda: askdirectory1())
btn1.grid(row=0, column=0, padx=(20,0), pady=(100,0))

btn2 = Button(root, text="Destination",width=10,height=1,font=('Times New Roman',13), command=lambda: askdirectory2())
btn2.grid(row=1, column=0, padx=(20,0), pady=(20,0))

btn3 = Button(root, text="Move files",width=15,height=1,font=('Times New Roman',13), command=lambda: getTxtFile())
btn3.grid(row=2, column=1, padx=(0,0), pady=(10,20), sticky=SE)


txt1 = Text(root, height=1, width=55)
txt1.grid(row=0,column=1, padx=(20,0), pady=(100,0))

txt2 = Text(root, height=1, width=55)
txt2.grid(row=1,column=1, padx=(20,0), pady=(20,0))



def askdirectory1():
    filepath=filedialog.askdirectory()
    sourcePath.set(filepath)
    txt1.insert(END, sourcePath.get())

def askdirectory2():
    filepath=filedialog.askdirectory()
    destPath.set(filepath)
    txt2.insert(END, destPath.get())


def getTxtFile():
    source = sourcePath.get()
    if source=="":
        print("Please choose source directory")
    destination = destPath.get()
    if destination=="":
        print("Please choose destination directory")
    files = os.listdir(source)
    
    for i in files:
        name, ext = os.path.splitext(i)
        if ext == ".txt":
           abspath = os.path.join(source, i)
           dest=shutil.move(abspath,destination)


    conn = sqlite3.connect("test.db")

    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_info( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_txt TEXT, \
            col_date_time)")
        conn.commit()
    conn.close()



    conn = sqlite3.connect("test.db")

    with conn:
        files = os.listdir(destination)
        for file in files:
            name, ext = os.path.splitext(file)
            if ext == ".txt":
                filepath = os.path.join(destination, file)
                time = os.path.getmtime(filepath)
            
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_info (col_txt, col_date_time) VALUES (?,?)", (file,time))
    conn.commit()

    cur.execute("SELECT col_txt, col_date_time FROM tbl_info")
    txtList = cur.fetchall()
    print (txtList)
    conn.close()
            

    


root.mainloop()




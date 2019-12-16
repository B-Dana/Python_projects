

import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.geometry('{}x{}'.format(670, 250))
        self.master.title("Check files")
        

        self.varBrowse1 = StringVar()
        self.varBrowse2 = StringVar()

        self.btnBrowse1 = Button(self.master, text="Browse...", width=15, height=1, font=("Times New Roman",13))
        self.btnBrowse1.grid(row=0, column=0, padx=(20,0), pady=(70,10))

        self.btnBrowse2 = Button(self.master, text="Browse...", width=15, height=1, font=("Times New Roman",13))
        self.btnBrowse2.grid(row=1, column=0, padx=(20,0), pady=(10,10))

        self.btnCheck = Button(self.master, text="Check for files...", width=15, height=2, font=("Times New Roman",13))
        self.btnCheck.grid(row=2, column=0, padx=(20,0), pady=(10,0), sticky=SW)

        self.btnClose = Button(self.master, text="Close Program", width=15, height=2, font=("Times New Roman",13))
        self.btnClose.grid(row=2, column=2, padx=(100,0), pady=(10,0), sticky=SE)


        self.txtBrowse1 = Entry(self.master, text=self.varBrowse1, width=35, font=("Helvetica",14))
        self.txtBrowse1.grid(row=0, column=2, padx=(40,0), pady=(60,5))

        self.txtBrowse2 = Entry(self.master, text=self.varBrowse2, width=35, font=("Helvetica",14))
        self.txtBrowse2.grid(row=1, column=2, padx=(40,0), pady=(0,0))





     

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

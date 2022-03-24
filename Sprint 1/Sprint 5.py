from tkinter import Tk, Label, Button
from tkinter import *
import tkinter.font as tkFont

class MainPage:
    def __init__(self, master):
        #setting title
        self.master = master
        master.title("Main")
        master.geometry("600x343")
        master.resizable(width=False, height=False)

        global counter
        global Label1

        counter = 0

        ft1 = tkFont.Font(family='Times', size=28)

        Label1 = Label(master, borderwidth="4px", font=ft1, fg="#333333", justify="center", text="0")
        Label1.grid(row=0, column=0, padx=10, ipady=60)

        ClickButton = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="CLICK HERE!", command= self.increaseCount)
        ClickButton.grid(row=1, column=0, padx=10, ipadx=157)  

        ExitButton = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="CLICK TO EXIT",  command= master.quit)
        ExitButton.grid(row=2, column=0, padx=10, ipadx=140)

    def increaseCount(self):
        
        global counter

        counter = counter + 1

        Label1.config(text="")
        Label1.config(text=counter)


root = Tk()
my_gui = MainPage(root)
root.mainloop()
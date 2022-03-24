import tkinter as tk
from tkinter import Tk, Label, Button, messagebox
from tkinter import *
import tkinter.font as tkFont

class MainPage:
    def __init__(self, master):
        #setting title
        self.master = master
        master.title("Main")
        master.geometry("233x380")
        master.resizable(width=False, height=False)

        ft1 = tkFont.Font(family='Times', size=18)
        ft2 = tkFont.Font(family='Times', size=10)

        global LabelEquation
        global LabelAnswer

        LabelEquation = Label(master, borderwidth="4px", bg="#ffffff", font=ft2, fg="#333333", width=32)
        LabelEquation.grid(row=0, columnspan=4, pady=2)

        LabelAnswer = Label(master, borderwidth="4px", bg="#ffffff", font=ft2, fg="#333333", width=32)
        LabelAnswer.grid(row=1, columnspan=4, pady=2)

        ExitButton = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="Exit", command= master.quit)
        ExitButton.grid(row=7, column=0, columnspan=4, ipadx= 83)

        ClearButton = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="Clear", command= lambda: self.clearText())
        ClearButton.grid(row=6, column=0, columnspan=2, ipadx= 19)

        EqualToButton = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="=", command= lambda: self.calcEquation())
        EqualToButton.grid(row=6, column=2, columnspan=2, ipadx= 39)

        ButtonDot = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text=".", command= lambda: self.receiveInput(ButtonDot))
        ButtonDot.grid(row=5, columnspan=2, ipadx= 42)

        ButtonNo0 = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="0", command= lambda: self.receiveInput(ButtonNo0))
        ButtonNo0.grid(row=5, column=2, ipadx= 10)

        ButtonNo1 = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="1", command= lambda: self.receiveInput(ButtonNo1))
        ButtonNo1.grid(row=4, column=0, ipadx= 10)  

        ButtonNo2 = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="2", command= lambda: self.receiveInput(ButtonNo2))
        ButtonNo2.grid(row=4, column=1, ipadx= 10)
        
        ButtonNo3 = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="3", command= lambda: self.receiveInput(ButtonNo3))
        ButtonNo3.grid(row=4, column=2, ipadx= 10)

        ButtonNo4 = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="4", command= lambda: self.receiveInput(ButtonNo4))
        ButtonNo4.grid(row=3, column=0, ipadx= 10)

        ButtonNo5 = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="5", command= lambda: self.receiveInput(ButtonNo5))
        ButtonNo5.grid(row=3, column=1, ipadx= 10)

        ButtonNo6 = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="6", command= lambda: self.receiveInput(ButtonNo6))
        ButtonNo6.grid(row=3, column=2, ipadx= 10)

        ButtonNo7 = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="7", command= lambda: self.receiveInput(ButtonNo7))
        ButtonNo7.grid(row=2, column=0, ipadx= 10)

        ButtonNo8 = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="8", command= lambda: self.receiveInput(ButtonNo8))
        ButtonNo8.grid(row=2, column=1, ipadx= 10)

        ButtonNo9 = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="9", command= lambda: self.receiveInput(ButtonNo9))
        ButtonNo9.grid(row=2, column=2, ipadx= 10)

        ButtonAddition = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="+", command= lambda: self.receiveInput(ButtonAddition))
        ButtonAddition.grid(row=5, column=3, ipadx= 10)  
        
        ButtonSubtraction = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="-", command= lambda: self.receiveInput(ButtonSubtraction))
        ButtonSubtraction.grid(row=4, column=3, ipadx= 12)

        ButtonMultiplication = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="*", command= lambda: self.receiveInput(ButtonMultiplication))
        ButtonMultiplication.grid(row=3, column=3, ipadx= 10)

        ButtonDivision = Button(master, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="/", command= lambda: self.receiveInput(ButtonDivision))
        ButtonDivision.grid(row=2, column=3, ipadx= 13)

    def receiveInput(self, button):

        currentLblText = LabelEquation.cget("text")
        currentButtonText = button.cget("text")
        #index = len(currentLblText)

        #if currentLblText == "":
        LabelEquation.config(text="")
        currentButtonText = button.cget("text")
        newEquation = str(currentLblText) + str(currentButtonText)
        LabelEquation.config(text=newEquation, width=32)
        #elif currentButtonText.isNumeric() == False or currentButtonText != "." and  currentLblText[index - 1] == "+" or "-" or "*" or "/":
           # messagebox.showerror(title="error",message="Please click a numeric value, you cannot use to mathematical signs in succession.")
       # else:
            #LabelEquation.config(text="")
            
            #newEquation = str(currentLblText) + str(currentButtonText)
            #LabelEquation.config(text=newEquation) 

    def calcEquation(self):
        
        newEquation = LabelEquation.cget("text")
        try:
            answer = eval(newEquation)
            LabelAnswer.config(text=answer, width=32)
        except:
            LabelAnswer.config(text="Error", width=32)
            answer = ""

    def clearText(self):
        LabelEquation.config(text="", width=32)
        LabelAnswer.config(text="", width=32)

root = Tk()
my_gui = MainPage(root)
root.mainloop()
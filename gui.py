from Tkinter import *
import tkMessageBox
from time import sleep

top = Tk()

L1 = Label(top, text="User Name")
L1.pack(side=LEFT)
E1 = Entry(top, bd=1)
E1.pack(side=RIGHT)

var = StringVar()
label = Label(top, textvariable=var, relief=RAISED)

var.set("Click below to see if your connection is working. You have one minute.")

label.pack()


if E1.get() == "Hannah":
    top.mainloop()
elif E1 != "Hannah":
    sleep(60)
    quit()


def connectionText():

    tkMessageBox.showinfo("Attempt Connection", "Connection Made!")


B1 = Button(top, text="Attempt Connection", command=connectionText, width=20)

B1.pack(side="left")

B2 = Button(top, text="Exit", fg="red", command=quit, width=10)
B2.pack(side="left")

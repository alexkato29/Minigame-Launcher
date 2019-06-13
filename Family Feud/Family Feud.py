"""from tkinter import *

root1 = Tk()
#root1.geometry("500x200")
root1.title("MAIN WINDOW")
canvas = Canvas(root1, bg="black")
canvas.grid()

def changeColor():
    canvas["bg"] = "red"

root2 = Tk()
root2.geometry("250x100")
root2.title("SUB WINDOW")

bttn1 = Button(root2, text="Push", command=changeColor)
bttn1.grid(row=0, column=0)

root2.mainloop()
root1.mainloop()
"""
import winsound

winsound.PlaySound("Theme Song Complete.wav", winsound.SND_FILENAME)
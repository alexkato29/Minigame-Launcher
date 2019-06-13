from GreenGlob import Coordinate as coord
from GreenGlob import greenGlob as g


import tkinter as tk

def create_grid(event=None):
    w = c.winfo_width()
    h = c.winfo_height()

    print("TEST" + str(w))
    xAxis = h/2 - (h/2 % 100)
    yAxis = w/2 - (w/2 % 100)

    globs = []

    for x in range(0, 10):
        newGlob = g.GreenGlob(w, h)
        globs.append(newGlob)

    for i in range(0, w, 100):
        if i == yAxis:
            c.create_line([(i, 0), (i, h)], tag='grid_line', fill="black")
        else:
            c.create_line([(i, 0), (i, h)], tag='grid_line', fill="grey")

    for i in range(0, h, 100):
        if i == xAxis:
            c.create_line([(0, i), (w, i)], tag='grid_line', fill="black")
        else:
            c.create_line([(0, i), (w, i)], tag='grid_line', fill="grey")

    for glob in globs:
        c.create_oval([(glob.xCoord - 15, glob.yCoord - 15), (glob.xCoord + 15, glob.yCoord + 15)], fill="green")


root = tk.Tk()

c = tk.Canvas(root, height=1000, width=1000, bg='white')
c.pack(fill=tk.BOTH, expand=True)

c.bind('<Configure>', create_grid)

w = c.winfo_width()
h = c.winfo_height()

root.mainloop()

# inputFunc = input("Please enter a Function: ")
# func = lambda z: eval(inputFunc.replace("x", str(z)))
# prevCoord = coord.Coordinate(0, func(0))
#
# print(w)
#
# for x in range(0, w, 5):
#     print("test")
#     newCoord = coord.Coordinate(x, func(x))
#     c.create_line([(int(prevCoord.x), int(prevCoord.y)), (int(newCoord.x), int(newCoord.y))], tag='grid_line', fill="black")
#     prevCoord = newCoord
#
# root.mainloop()

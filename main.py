from GreenGlob import greenGlob as g

import tkinter as tk

def create_grid(event=None):
    w = c.winfo_width()
    h = c.winfo_height()

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

root.mainloop()
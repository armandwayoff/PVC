from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from random import *

root = Tk()
root.title("TSP Solver")
root.geometry("800x600")
root.minsize(800, 600)

fig = Figure(figsize=(5, 5), dpi=100)
new_plot = fig.add_subplot(111)


def new_random_plot():
    x = [randint(0, 10) for _ in range(25)]
    y = [randint(0, 10) for _ in range(25)]
    new_plot.clear()
    new_plot.scatter(x, y, c="black")


canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=TRUE)


label_frame = LabelFrame(root, text="Parameters", width=300, height=800).pack(side=RIGHT, expand='no', fill='y')
button = Button(label_frame, text="NEW", command=new_random_plot).pack()

root.mainloop()

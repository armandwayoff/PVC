from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from random import *

root = Tk()
root.title("TSP Solver")
root.geometry("800x600")
root.minsize(800, 600)

fig = Figure(figsize=(5, 5), dpi=100)
new_plot = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)


def new_random_plot():
    x = [uniform(0, 10) for _ in range(50)]
    y = [uniform(0, 10) for _ in range(50)]
    new_plot.clear()
    new_plot.scatter(x, y, c="black")
    canvas.draw()
    canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=TRUE)


parameters_frame = LabelFrame(root, text="Parameters", width=300, height=800, bg='white')
parameters_frame.pack(side=RIGHT, expand=0, fill=Y)
new_random_plot_button = Button(parameters_frame, text="New random plot", command=new_random_plot).pack()

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()

root.mainloop()

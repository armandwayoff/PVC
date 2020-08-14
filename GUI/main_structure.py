from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

root = Tk()
root.geometry("800x600")
root.title("TSP Solver")


def plot():
    fig = Figure(figsize=(5, 5), dpi=100)
    y = [i ** 2 for i in range(101)]
    plot1 = fig.add_subplot(111)
    plot1.plot(y)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    # canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=TRUE)
    # toolbar = NavigationToolbar2Tk(canvas, root)
    # toolbar.update()
    canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=TRUE)


parameters_frame = Frame(root, width=200, height=500, bg="blue").pack(side="right", fill=BOTH, expand=TRUE)

plot()
root.mainloop()

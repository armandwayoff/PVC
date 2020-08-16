from tkinter import *
from tkinter.ttk import Combobox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from random import *

root = Tk()
root.title("TSP Solver")
root.geometry("800x600")
root.minsize(800, 600)


def new_random_plot():
    x = [uniform(0, 10) for _ in range(50)]
    y = [uniform(0, 10) for _ in range(50)]
    new_plot.clear()
    new_plot.scatter(x, y, c="black")
    canvas.draw()


# Parameters

parameters_frame = LabelFrame(root, text="Parameters", width=300, height=800, bg='white')
parameters_frame.pack(side=RIGHT, expand=0, fill=Y)

# Data
label1 = Label(parameters_frame, text="Data", bg="white").pack()
import_data_button = Button(parameters_frame, text="Import data").pack()
new_random_plot_button = Button(parameters_frame, text="New random plot", command=new_random_plot).pack()

# Initialisation algorithm
label2 = Label(parameters_frame, text="Initialisation algorithm", bg="white").pack()
initialisation_algorithms = ["Random", "Nearest neighbour algorithm"]
selection = Combobox(parameters_frame, values=initialisation_algorithms)
selection.current(0)
selection.pack()

# Solving algorithm
label3 = Label(parameters_frame, text="Solving algorithm", bg="white").pack()
solving_algorithms = ["2-opt", "Simulated annealing", "Brute-force search"]
selection1 = Combobox(parameters_frame, values=solving_algorithms)
selection1.current(0)
selection1.pack()

# Solve button
solve_button = Button(parameters_frame, text="Solve", bg='limegreen').pack()

# Graph

fig = Figure(figsize=(5, 5), dpi=100)
new_plot = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=TRUE)

root.mainloop()

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from random import *

root = Tk()
root.title("TSP Solver")
root.iconbitmap('icon.ico')
root.geometry("800x600")
root.minsize(800, 600)

global x, y


def new_random_plot():
    x = [uniform(0, 10) for _ in range(50)]
    y = [uniform(0, 10) for _ in range(50)]
    new_plot.clear()
    new_plot.scatter(x, y, c="black")
    canvas.draw()


def solve():
    # Initialisation process
    if initialisation_algorithm.get() == "Random":
        print(1)
    elif initialisation_algorithm.get() == "Nearest neighbour algorithm":
        print(2)
    else:
        messagebox.showerror("Error", "The selected initialization algorithm is not valid")


# Parameters
parameters_frame = LabelFrame(root, text="Parameters", width=300, height=800, bg='white')
parameters_frame.pack(side=RIGHT, expand=0, fill=Y)

# Data
data_label = Label(parameters_frame, text="Data", bg="white").pack()
import_data_button = Button(parameters_frame, text="Import data").pack()
new_random_plot_button = Button(parameters_frame, text="New random plot", command=new_random_plot).pack()

# Initialisation algorithms
initialisation_algorithms_label = Label(parameters_frame, text="Initialisation algorithm", bg="white").pack()
initialisation_algorithms_lst = ["Random", "Nearest neighbour algorithm"]
initialisation_algorithm = StringVar()
initialisation_algorithms_combobox = Combobox(parameters_frame,
                                              values=initialisation_algorithms_lst,
                                              textvariable=initialisation_algorithm)
initialisation_algorithms_combobox.current(0)
initialisation_algorithms_combobox.pack()

# Solving algorithms
solving_algorithms_label = Label(parameters_frame, text="Solving algorithm", bg="white").pack()
solving_algorithms_lst = ["2-opt", "Simulated annealing", "Brute-force search"]
solving_algorithm = StringVar()
solving_algorithms_combobox = Combobox(parameters_frame,
                                       values=solving_algorithms_lst,
                                       textvariable=solving_algorithm)
solving_algorithms_combobox.current(0)
solving_algorithms_combobox.pack()

# Solve button
solve_button = Button(parameters_frame, text="Solve", bg='limegreen', command=solve).pack()

# Graph

fig = Figure(figsize=(5, 5), dpi=100)
new_plot = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=TRUE)

root.mainloop()

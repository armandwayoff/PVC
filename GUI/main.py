from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from algorithms import *

# style constants
FONT = "Arial"
H1 = 15
H2 = 12
MAIN_BG_COL = "white"

root = Tk()
root.title("TSP Solver")
root.iconbitmap('icon.ico')
root.geometry("800x600")
root.minsize(800, 600)


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


n = 10


def import_data():
    def open_files():
        root.filename = filedialog.askopenfilename()
        import_data_page_button.config(text="Select new file")
        import_data_page_label.config(text="Selected file : " + str(root.filename))
        quit_button.config(text="OK")
    # Create pop-up window
    import_data_page = Toplevel(root)
    import_data_page.title("Import data")
    import_data_page.iconbitmap('icon.ico')
    import_data_page.geometry("300x80")
    import_data_page.resizable(True, False)
    import_data_page.attributes("-topmost", "true")

    import_data_page_button = Button(import_data_page, text="Select file", command=open_files, relief=GROOVE)
    import_data_page_button.pack()
    import_data_page_label = Label(import_data_page, text="")
    import_data_page_label.pack()
    quit_button = Button(import_data_page, text="Cancel", relief=GROOVE, command=import_data_page.destroy)
    quit_button.pack()


def new_random_data():
    vertices = []
    x = [uniform(0, 10) for _ in range(n)]
    y = [uniform(0, 10) for _ in range(n)]
    for i in range(n):
        vertices.append(Vertex(x[i], y[i]))
    display(vertices)


def display(path):
    plot.clear()
    for i in range(len(path) - 1):
        plot.plot([path[i].x, path[i + 1].x], [path[i].y, path[i + 1].y], 'b')
    for vertex in path:
        plot.plot(vertex.x, vertex.y, 'bo')
    canvas.draw()


def solve():
    # Initialisation process
    if initialization_algorithm.get() == "Random":
        print(1)
    elif initialization_algorithm.get() == "Nearest neighbour algorithm":
        print(2)
    else:
        messagebox.showerror("Error", "The selected initialization algorithm is not valid")


# Parameters
parameters_frame = LabelFrame(root, width=300, height=800, bg=MAIN_BG_COL)
parameters_frame.pack(side=RIGHT, expand=0, fill=Y)

# Data
data_label = Label(parameters_frame, text="Data", bg=MAIN_BG_COL)
data_label.grid(row=0, column=0)

import_data_button = Button(parameters_frame, text="Import data", relief=GROOVE, command=import_data)
import_data_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
new_random_plot_button = Button(parameters_frame, text="New random data", relief=GROOVE, command=new_random_data)
new_random_plot_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Initialization algorithms
initialization_algorithms_label = Label(parameters_frame, text="Initialization algorithm :", bg=MAIN_BG_COL)
initialization_algorithms_label.grid(row=3, column=0)
initialization_algorithms_lst = ["Random", "Nearest neighbour algorithm"]
initialization_algorithm = StringVar()
initialization_algorithms_combobox = Combobox(parameters_frame,
                                              values=initialization_algorithms_lst,
                                              textvariable=initialization_algorithm)
initialization_algorithms_combobox.current(0)
initialization_algorithms_combobox.grid(row=3, column=1)

# Solving algorithms
solving_algorithms_label = Label(parameters_frame, text="Solving algorithm :", bg=MAIN_BG_COL)
solving_algorithms_label.grid(row=4, column=0)
solving_algorithms_lst = ["2-opt", "Simulated annealing", "Brute-force search"]
solving_algorithm = StringVar()
solving_algorithms_combobox = Combobox(parameters_frame, values=solving_algorithms_lst, textvariable=solving_algorithm)
solving_algorithms_combobox.current(0)
solving_algorithms_combobox.grid(row=4, column=1)

# Solve button
solve_button = Button(parameters_frame, text="Solve", width=15, bg='limegreen', relief=GROOVE, command=solve)
solve_button.grid(row=5, column=0, columnspan=2, pady=350)

# Graph
fig = Figure(figsize=(5, 5), dpi=100)
plot = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=TRUE)

root.mainloop()

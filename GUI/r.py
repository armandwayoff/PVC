from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from algorithms import *

# Creation of the main window
root = Tk()
root.title("TSP Solver")
root.iconbitmap('icon.ico')
root.geometry("800x600")
root.minsize(800, 600)


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def import_data():
    # Create pop-up window
    import_data_page = Toplevel(root)
    import_data_page.grab_set()
    import_data_page.title("Import data")
    import_data_page.iconbitmap('icon.ico')
    import_data_page.geometry("300x80")
    import_data_page.resizable(True, False)

    import_data_page_button = Button(import_data_page, text="Select file", command=open_files, relief=GROOVE)
    import_data_page_button.pack()
    import_data_page_label = Label(import_data_page, text="")
    import_data_page_label.pack()
    quit_button = Button(import_data_page, text="Cancel", relief=GROOVE, command=import_data_page.destroy)
    quit_button.pack()


def open_files():
    root.filename = filedialog.askopenfilename()


def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def new_random_data():
    vertices = []
    if is_int(spin.get()):
        number_vertices = int(spin.get())
        x = [uniform(0, 10) for _ in range(number_vertices)]
        y = [uniform(0, 10) for _ in range(number_vertices)]
        for i in range(number_vertices):
            vertices.append(Vertex(x[i], y[i]))
        display(vertices)
    else:
        messagebox.showerror("Error", "Number of vertices is invalid")


def display(path):
    plot.clear()
    #for i in range(len(path) - 1):
    #    plot.plot([path[i].x, path[i + 1].x], [path[i].y, path[i + 1].y], 'b')
    for vertex in path:
        plot.plot(vertex.x, vertex.y, 'bo')
    canvas.draw()


def solve():
    # Initialisation process
    if init_alg.get() == "Random":
        messagebox.askquestion("Validation", "Do you confirm the parameters ?")
    elif init_alg.get() == "Nearest neighbour algorithm":
        messagebox.askquestion("Validation", "Do you confirm the parameters ?")
    else:
        messagebox.showerror("Error", "The selected initialization algorithm is not valid")


# User frame
user_frame = LabelFrame(root, width=300, height=800)
user_frame.pack(side=RIGHT, expand=0, fill=Y)


def data_button():
    global but
    if data_mode.get() == "import-data":
        but.config(text="Select file")
        but.config(command=open_files)
    else:
        but.config(text="Generate random data")
        but.config(command=new_random_data)


# Data frame
data_frame = LabelFrame(user_frame, text="Data")
data_frame.grid(row=0, column=0)

data_mode = StringVar()
import_data_button = Radiobutton(data_frame, text="Import data", relief=GROOVE, variable=data_mode, value="import-data", command=data_button)
import_data_button.grid(row=1, column=0)
new_random_plot_button = Radiobutton(data_frame, text="Random data", relief=GROOVE, variable=data_mode, value="random-data", command=data_button)
new_random_plot_button.grid(row=1, column=1)
import_data_button.select()

but = Button(data_frame, text="Select file", relief=GROOVE, command=open_files)
but.grid(row=2, column=0, columnspan=2)
Label(data_frame, text="Number of vertices :").grid(row=3, column=0)
spin = Spinbox(data_frame, from_=3, to=100, width=4)
spin.grid(row=3, column=1)

# Parameters frame
parameters_frame = LabelFrame(user_frame, text="Parameters")
parameters_frame.grid(row=1, column=0)

# Initialization algorithms
init_alg_label = Label(parameters_frame, text="Initialization algorithm :")
init_alg_label.grid(row=3, column=0)
init_alg_lst = ["Random", "Nearest neighbour algorithm"]
init_alg = StringVar()
init_alg_combobox = Combobox(parameters_frame, values=init_alg_lst, textvariable=init_alg)
init_alg_combobox.current(0)
init_alg_combobox.grid(row=3, column=1)

# Solving algorithms
solving_alg_label = Label(parameters_frame, text="Solving algorithm :")
solving_alg_label.grid(row=4, column=0)
solving_alg_lst = ["2-opt", "Simulated annealing", "Brute-force search"]
solving_alg = StringVar()
solving_alg_combobox = Combobox(parameters_frame, values=solving_alg_lst, textvariable=solving_alg)
solving_alg_combobox.current(0)
solving_alg_combobox.grid(row=4, column=1)

# Solve button
solve_button = Button(user_frame, text="Solve", width=15, bg='limegreen', relief=GROOVE, command=solve)
solve_button.grid(row=5, column=0, columnspan=2, pady=350)

# Graph frame
fig = Figure(figsize=(5, 5), dpi=100)
plot = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=TRUE)

root.mainloop()

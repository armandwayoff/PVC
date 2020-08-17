"""
 *- TSP SOLVER -*

 built by Armand WAYOFF
"""

from tkinter import *
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# Creation of the main window
root = Tk()
root.title("TSP Solver")
root.iconbitmap('icon.ico')
root.geometry("800x600")
root.minsize(800, 600)


def open_files():
    root.filename = filedialog.askopenfilename()
    if len(root.filename) > 20:
        file_name = str(root.filename[-20:])
    else:
        file_name = str(root.filename)
    label.config(text="Selected file : " + file_name)


# User frame
user_frame = LabelFrame(root, width=300, height=800, padx=10, pady=10)
user_frame.pack(side=RIGHT, expand=0, fill=Y)

def data_button():
    global spin
    if data_mode.get() == "import-data":
        button.config(text="Select file")
        button.config(command=open_files)
        label.config(text="Selected file :")
        spin.grid_remove()
    else:
        button.config(text="Generate random data")
        label.config(text="Number of vertices :")
        spin = Spinbox(data_frame, from_=3, to=100, width=4)
        spin.grid(row=3, column=1, sticky=W)


# Data frame
data_frame = LabelFrame(user_frame, text="Data", width=215, height=100)
data_frame.grid(row=0, column=0)
data_frame.grid_propagate(1)

data_mode = StringVar()
import_data_button = Radiobutton(data_frame, text="Import data", width=10, relief=GROOVE, variable=data_mode, value="import-data", command=data_button)
import_data_button.grid(row=1, column=0, sticky=NSEW)
new_random_plot_button = Radiobutton(data_frame, text="Random data", width=10, relief=GROOVE, variable=data_mode, value="random-data", command=data_button)
new_random_plot_button.grid(row=1, column=1, sticky=NSEW)
import_data_button.select()

button = Button(data_frame, text="Select file", relief=GROOVE, command=open_files)
button.grid(row=2, column=0, columnspan=2, sticky=W+E)
label = Label(data_frame, text="Selected file :")
label.grid(row=3, column=0, columnspan=2)

# Graph frame
fig = Figure(figsize=(5, 5), dpi=100)
plot = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=TRUE)

root.mainloop()

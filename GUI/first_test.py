from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

app = Tk()
app.title("TSP Solver")
app.geometry("800x600")

label_title = Label(app, text="Travelling Salesman Problem Solver", font=("Arial", 18))
label_title.pack()

parameters_frame = LabelFrame(app, text="Parameters", width=300, height=600)
parameters_frame.pack()

combo = Combobox(parameters_frame)
combo['values']= ("2-opt", "Simulated Annealing", "Genetic Algorithm", "Brute-Force Search")
combo.current(0)
combo.pack()


def confirmation():
    messagebox.askokcancel("Confirmation", "Are you sure of the parameters you have entered ?")


button_solver = Button(parameters_frame, text="Solve", command=confirmation)
button_solver.pack()

label_author = Label(app, text="Built by Armand Wayoff")
label_author.pack()

app.mainloop()

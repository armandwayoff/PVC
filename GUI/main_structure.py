from tkinter import *

root = Tk()
root.geometry("800x600")
root.title("TSP Solver")

title_frame = Frame(root, width=800, height=100, bg="gainsboro").pack(side=TOP, fill=X)

graph_frame = Frame(root, width=600, height=500, bg="red").pack(side=LEFT, fill=BOTH, expand=TRUE)

parameters_frame = Frame(root, width=200, height=500, bg="blue").pack(side="right", fill=BOTH, expand=TRUE)

root.mainloop()

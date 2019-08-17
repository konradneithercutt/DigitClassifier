import matplotlib
from tkinter import *
from tkinter import ttk
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure

# Importing stuff I've written
import classifier


class GUI(object):



    def __init__(self):
        self.classifier = classifier.Classifier()
        root = Tk()
        root.title("Random Digit Display")
        mainframe = ttk.Frame(root, padding="3 3 12 12")


        mainframe.grid(column=0, row=0, sticky=(N, W, S, E))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Button(mainframe, text="Show Digit").grid(column=3, row=3, sticky=(N))
        root.mainloop()

    def show_random_digit():
        # has to get a figure from the classifier, add it to canvas
        return


if __name__ == "__main__":
    GUI()

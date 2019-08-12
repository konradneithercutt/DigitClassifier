from tkinter import *
from tkinter import ttk

class Classifier(object):

    canvas = None


    def __init__(self):
        root = Tk()
        root.title("Random Digit Display")
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, S, E))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Button(mainframe, text="Show Digit").grid(column=1, row=1, sticky=(N))
        root.mainloop()

    def show_digit():
        return


if __name__ == "__main__":
    Classifier()

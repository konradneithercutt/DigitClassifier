from tkinter import *
from tkinter import ttk

class Classifier(object):

    def __init__(self):
        root = Tk()
        ttk.Button(root, text="Hello World").grid()
        root.mainloop()


if __name__ == "__main__":
    Classifier()

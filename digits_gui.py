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

        self.gold_display = StringVar()
        self.predicted_display = StringVar()

        ttk.Label(mainframe, textvariable=self.gold_display).grid(column=0, row=1, sticky=(S, W))
        ttk.Label(mainframe, textvariable=self.predicted_display).grid(column=0, row=2, sticky=(N, E))

        ttk.Button(mainframe, text="Show Digit", command=self.show_random_digit).grid(column=3, row=3, sticky=(N))
        root.mainloop()
    # def calculate(self, *args):
    #     try:
    #         value = float(self.feet.get())
    #         self.meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    #     except ValueError:
    #         pass


    def show_random_digit(self):
        # has to get a figure from the classifier, add it to canvas
        image_data, gold_label, predicted_label = self.classifier.get_random_digit()

        self.gold_display.set(gold_label)
        self.predicted_display.set(predicted_label)
        return
        # ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
        # ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)
        #
        # ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        # ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        # ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

if __name__ == "__main__":
    GUI()

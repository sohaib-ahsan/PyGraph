import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)


def matplotter(window, eq, cgrid, cgraph):
    x = np.linspace(-100, 100, 1000)
    fig = plt.figure(figsize=(10, 10))

    y2 = 0*x
    plt.plot(x, y2, color=cgrid)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    x1 = 0*x
    plt.plot(x1,x,color = cgrid)
    canvas.get_tk_widget().pack()

    eq = eval(eq)
    y = eq
    plt.plot(x, y, color=cgraph)
    # Add features to our figure

    plt.grid(True)
    plt.xlim([-10, 10])
    plt.ylim([-10,10])
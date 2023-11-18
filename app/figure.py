import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def plot(orgList, len):
    plt.style.use('_mpl-gallery')
    x = np.arange(0, len, 1)
    y = np.vstack(orgList)

    fig, ax = plt.subplots()
    ax.stackplot(x, y)

    plt.show()








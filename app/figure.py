import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

# plt.rcParams["figure.autolayout"] = True

# import textwrap
# def wrap_labels(ax, width, break_long_words=False):
#     labels = []
#     for label in ax.get_xticklabels():
#         text = label.get_text()
#         labels.append(textwrap.fill(text, width=width,
#                       break_long_words=break_long_words))
#     ax.set_xticklabels(labels, rotation=0)

import textwrap
def wrap_labels(ax, length, break_long_words=False):
    labels = []
    for label in ax.get_xticklabels():
        text = label.get_text()
        labels.append(textwrap.fill(text, width=length,
                      break_long_words=break_long_words))
    ax.set_xticklabels(labels, rotation=75)

def plot(orgList, len):
    plt.rcParams.update({'font.size': 22})
    plt.rcParams["figure.figsize"] = [120,50]

    x = np.arange(0, len, 1)
    xticks = orgList[2]
    y = np.vstack(orgList[0])
    # y = np.array(orgList[0])

    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=10)
    ax.set_ylabel("# of records lost", fontsize=60)
    ax.set_xlabel("organization", fontsize=60, wrap=True)
    ax.get_yaxis().get_major_formatter().set_scientific(False)
    ax.tick_params(axis='y', labelsize=60)
    ax.grid(True)

    plt.xticks(x, xticks, rotation=75, wrap=True)
    if (len<50):
        wrap_labels(ax, 10)
    fig.savefig("static/my_plot.png")
    







"""
Set ticker properties
http://matplotlib.org/api/ticker_api.html
"""
import numpy as np

import matplotlib
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

import matplotlib.ticker as mticker

fig = figure.Figure()
canvas = FigureCanvas(fig)

ax = fig.add_subplot(1,1,1)

data = np.random.randint(1,10, size=(2,100))

ax.scatter(data[0], data[1], s=100)

ax.set_xticks(range(1,10))
ax.set_xticklabels(['one', 'two', 'three', 'four',
                               'five', 'six', 'seven', 'eight', 
							   'nine'])

yloc = mticker.IndexLocator(3,0)
yfmt = mticker.FormatStrFormatter("val=%d")
ax.yaxis.set_major_formatter(yfmt)
ax.yaxis.set_major_locator(yloc)
ax.tick_params(axis='y', colors='red', labelsize='15')

canvas.print_figure('../figures/textnomticker.png', 
		facecolor='lightgray')
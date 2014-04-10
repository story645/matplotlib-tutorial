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

xfmt = mticker.FixedFormatter(['one', 'two', 'three', 'four',
                               'five', 'six', 'seven', 'eight', 
							   'nine'])
ax.xaxis.set_major_formatter(xfmt)
yfmt = mticker.FormatStrFormatter("val=%d")
ax.yaxis.set_major_formatter(yfmt)

canvas.print_figure('../figures/textform.png', 
		facecolor='lightgray')
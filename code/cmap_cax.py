"""
Example of matplotlib colormaps
http://matplotlib.org/api/figure_api.html#matplotlib.figure.Figure.colorbar
"""

import numpy as np

import matplotlib
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

data = np.random.randn(50,50)

fig = figure.Figure()

canvas = FigureCanvas(fig)

ax1 = fig.add_subplot(1,1,1)
plt1 = ax1.imshow(data, cmap='RdBu')
cbar = fig.colorbar(plt1, ax=ax1, fraction=0.045)
cbar.set_label("Random Data")

canvas.print_figure('../figures/cmapaxis.png', 
		facecolor='lightgray')
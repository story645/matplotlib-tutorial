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

fig = figure.Figure(figsize=(12,6))

canvas = FigureCanvas(fig)
#using kwargs
ax1 = fig.add_subplot(1,2,1)
plt1 = ax1.imshow(data, cmap='RdBu')
fig.colorbar(plt1, ax=ax1, fraction=0.045)

ax2 = fig.add_subplot(1,2,2)
plt2 = ax2.imshow(data, cmap='RdBu')
fig.colorbar(plt2, ax=ax2, fraction=0.04, orientation='horizontal')

canvas.print_figure('../figures/movedcmap.png', 
		facecolor='lightgray')
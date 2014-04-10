"""
Example of matplotlib colormaps
http://matplotlib.org/1.3.1/api/artist_api.html?highlight=lines#module-matplotlib.lines
"""

import numpy as np

import matplotlib
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

data = np.random.randn(50,50)

fig = figure.Figure(figsize=(12,6))

canvas = FigureCanvas(fig)

ax1 = fig.add_subplot(1,3,1)
plt1 = ax1.imshow(data, cmap='Blues')
fig.colorbar(plt1, ax=ax1)

ax2 = fig.add_subplot(1,3,2)
plt2 = ax2.imshow(data, cmap='Reds')
fig.colorbar(plt2, ax=ax2)

ax3 = fig.add_subplot(1,3,3)
plt3 = ax3.imshow(data, cmap='RdBu')
fig.colorbar(plt3, ax=ax3)

canvas.print_figure('../figures/basiccolor.png', 
		facecolor='lightgray')
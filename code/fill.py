"""
Example of creating a figure
"""
import numpy as np

from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

fig = figure.Figure(figsize=(20,10))

canvas = FigureCanvas(fig)

ax = fig.add_subplot(1,1,1)

x = np.arange(0,20,.01)
y = np.sin(x)
z = np.cos(x)
ax.plot(x,y)
ax.plot(x,z)
ax.fill_between(x,y,z, where=(z>y), color='r')
ax.fill_between(x,z,y, where=(y>z), color='y')
ax.axhline(color='k')

canvas.print_figure('../figures/canvas.png', 
		facecolor='lightgray')
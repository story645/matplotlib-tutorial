"""
Example of creating an empty subplot
"""
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)
#needed to support 3d projections/plots
from mpl_toolkits.mplot3d import Axes3D

fig = figure.Figure()

canvas = FigureCanvas(fig)

ax = fig.add_subplot(1,1,1)
ax.scatter(0.5, 0.55, s=1000, edgecolor='b', color='pink')
ax.scatter(0.53, 0.53, s=1000, edgecolor='pink', color='blue', 
	alpha=.5)

ax.set_ylim((0,1))
ax.set_xlim((0,1))
fig.tight_layout()

canvas.print_figure('../figures/pointalpha.png', 
		facecolor='lightgray')
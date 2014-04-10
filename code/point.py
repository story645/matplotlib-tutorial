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
ax.scatter(0.5, 0.5, s=500, edgecolor='b', color='pink')

fig.tight_layout()

canvas.print_figure('../figures/point.png', 
		facecolor='lightgray')
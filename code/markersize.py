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
i = range(1,100)
ax.scatter(i,i,s=i, color='y',edgecolor='k')


ax.set_ylim((0,100))
ax.set_xlim((0,100))
fig.tight_layout()

canvas.print_figure('../figures/markersize.png', 
		facecolor='lightgray')
"""
Example of manipulating each axis directly
"""
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)
#needed to support 3d projections/plots
from mpl_toolkits.mplot3d import Axes3D

fig = figure.Figure()

canvas = FigureCanvas(fig)

ax1 = fig.add_subplot(3,1,1)
ax1.xaxis.grid(True)
ax1.set_xlabel("X label")
ax1.set_xlim((-1, 1))

ax2 = fig.add_subplot(3,1,2)
ax2.yaxis.grid(True)
ax2.set_ylabel("Y label")
ax2.set_ylim((-1,1))

ax3 = fig.add_subplot(3,1,3, projection='3d')
ax3.zaxis.grid(True)
ax3.set_zlabel("Z label")
ax3.set_zlim((-1,1,))

fig.tight_layout()

canvas.print_figure('../figures/xyz.png', 
		facecolor='lightgray')
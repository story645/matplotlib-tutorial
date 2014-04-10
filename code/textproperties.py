"""
Set properties
"""


import matplotlib
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

fig = figure.Figure()
canvas = FigureCanvas(fig)

ax = fig.add_subplot(1,1,1)
ax.set_title(r'$\alpha=\beta$', fontsize=30, color='teal')

canvas.print_figure('../figures/textp.png', 
		facecolor='lightgray')
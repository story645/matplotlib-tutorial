"""
Example of Using Latex in fig titles
"""


import matplotlib
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

fig = figure.Figure()
canvas = FigureCanvas(fig)

ax = fig.add_subplot(1,1,1)
ax.set_title(r'$\alpha=\beta$')

canvas.print_figure('../figures/latex.png', 
		facecolor='lightgray')
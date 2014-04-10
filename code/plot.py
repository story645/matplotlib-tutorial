"""
Example of creating an empty subplot
"""
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

fig = figure.Figure()

canvas = FigureCanvas(fig)

ax = fig.add_subplot(1,1,1)

canvas.print_figure('../figures/plot.png', 
		facecolor='lightgray')
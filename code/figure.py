"""
Example of creating a figure
"""
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

fig = figure.Figure()

canvas = FigureCanvas(fig)

canvas.print_figure('../figures/canvas.png', 
		facecolor='lightgray')
"""
Example of matplotlib linestyles
http://matplotlib.org/1.3.1/api/artist_api.html?highlight=lines#module-matplotlib.lines
"""
import matplotlib
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

fig = figure.Figure(figsize=(12,6))

canvas = FigureCanvas(fig)

ax = fig.add_subplot(1,1,1)
#matplotlib can take any HTMLcolor
ax.scatter(.5, .5, color='#8ED9E1', s=500)
ax.set_xlim((0,1))
ax.set_ylim((0,1))
canvas.print_figure('../figures/pointcolor.png', 
		facecolor='lightgray')
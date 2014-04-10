"""
Example of matplotlib linestyles
http://matplotlib.org/1.3.1/api/artist_api.html?highlight=lines#module-matplotlib.lines
"""
import matplotlib
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)
#needed to support 3d projections/plots
from mpl_toolkits.mplot3d import Axes3D

fig = figure.Figure(figsize=(12,6))

canvas = FigureCanvas(fig)

ax = fig.add_subplot(1,1,1)
llist = matplotlib.lines.Line2D.lineStyles.keys()
print llist
pad=2
for i, l in enumerate(llist):
	ax.axvline(i+pad,0,1,linestyle=l, color='k',linewidth=2)
	#displays the m needed to make the marker
	ax.annotate(l, xy=(i+pad,.5), xytext=(i+(1.25*pad), .5),
				bbox=dict(boxstyle="round",fc='w'), 
				arrowprops=dict(arrowstyle="->"),
				horizontalalignment='right',
				fontsize=30
				)
	
#ax.set_xlim((0,1))
ax.set_ylim((0,1))
ax.set_xticks([])
ax.set_yticks([])
canvas.print_figure('../figures/linestyle.png', 
		facecolor='lightgray')
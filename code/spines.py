"""
Example of manipulating splines
"""
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

fig = figure.Figure()

canvas = FigureCanvas(fig)

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
for axis in ['top','bottom','left','right']:
  ax1.spines[axis].set_linewidth(5)
  ax2.spines[axis].set_linewidth(5)
  
#manipulate each spine-can also set it invisible  
ax1.spines['right'].set_color('r')
ax1.spines['top'].set_color('b')
ax1.spines['bottom'].set_color('g')
ax1.spines['left'].set_color('y')

#clear spines
ax2.spines['top'].set_color('none')
ax2.spines['right'].set_color('none')

fig.tight_layout()

canvas.print_figure('../figures/spines.png', 
		facecolor='lightgray')
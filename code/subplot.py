"""
Example of creating an empty subplot
"""
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

fig = figure.Figure()

canvas = FigureCanvas(fig)
#number rows, number columns, position
ax1 = fig.add_subplot(2,3,1)
ax1.text(.5,.5,"ax1")
ax2 = fig.add_subplot(2,3,2)
ax2.text(.5,.5,"ax2")
ax3 = fig.add_subplot(2,3,3)
ax3.text(.5,.5,"ax3")
ax4 = fig.add_subplot(2,3,4)
ax4.text(.5,.5,"ax4")
ax5 = fig.add_subplot(2,3,5)
ax5.text(.5,.5,"ax5")
ax6 = fig.add_subplot(2,3,6)
ax6.text(.5,.5,"ax6")

#fig.tight_layout()

canvas.print_figure('../figures/subplot.png', 
		facecolor='lightgray')
"""
Example of matplotlib markers
http://matplotlib.org/api/markers_api.html
"""
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)
#needed to support 3d projections/plots
from mpl_toolkits.mplot3d import Axes3D

fig = figure.Figure(figsize=(12,6))

canvas = FigureCanvas(fig)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
mlist = matplotlib.markers.MarkerStyle.markers.keys()
print mlist
pad=500
for i, m in enumerate(mlist):
	
	ax.scatter(i+pad, 0, marker=m, s=150, color='y', edgecolor='k')
	
	#displays the m needed to make the marker
	flip = i%2
	alt = ((i%4)*.1 + .2)*((-1)**(flip+1))
	ax.annotate(m, xy=(i+pad,0), xytext=(i+pad, alt),
				bbox=dict(boxstyle="round",fc='w'), 
				arrowprops=dict(arrowstyle="->"))
	
ax.set_ylim((-.5,.6))
ax.set_xlim((498,535))

ax.set_xticks([])
ax.set_yticks([])
plt.show()
canvas.print_figure('../figures/markerstyle.png', 
		facecolor='lightgray')

"""	
The marker can also be a tuple (numsides, style, angle), which will create a custom, regular symbol.

    numsides:
        the number of sides
    style:

        the style of the regular symbol:
        Value 	Description
        0 	a regular polygon
        1 	a star-like symbol
        2 	an asterisk
        3 	a circle (numsides and angle is ignored)
    angle:
        the angle of rotation of the symbol, in degrees

"""


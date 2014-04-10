"""
Example of matplotlib colormaps
http://matplotlib.org/api/colors_api.html
"""

import numpy as np

import matplotlib
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

import matplotlib.cm as mcm
import matplotlib.colors as mcolors

data = np.random.randn(50,50)



fig = figure.Figure()

canvas = FigureCanvas(fig)

#custom gradient
cmap = mcolors.LinearSegmentedColormap.from_list('from_list', 
          ['yellowgreen', 'hotpink'])
norm = mcolors.BoundaryNorm(np.arange(-2,3,1), cmap.N)
ax1 = fig.add_subplot(1,2,1)
plt1 = ax1.imshow(data, interpolation='nearest',
				  cmap=cmap, norm=norm)
cbar1 = fig.colorbar(plt1, ax=ax1, fraction=0.045)

#custom listed

cmap = mcolors.LinearSegmentedColormap.from_list('from_list', 
			['yellowgreen', 'teal', 'hotpink'])
			
norm = mcolors.BoundaryNorm([-3,-1,1,3], cmap.N)
ax2 = fig.add_subplot(1,2,2)
plt2 = ax2.imshow(data, interpolation='nearest', cmap=cmap, norm=norm)
cbar2 = fig.colorbar(plt2, ax=ax2, fraction=0.045)

fig.subplots_adjust(wspace=.4)
canvas.print_figure('../figures/cmapcustom.png', 
		facecolor='lightgray')

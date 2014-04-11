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

a = np.random.permutation(np.arange(10))
b = np.random.permutation(np.arange(10))
c = np.random.permutation(np.arange(10))
d = np.random.permutation(np.arange(0,10))

fig = figure.Figure()

canvas = FigureCanvas(fig)
cmap = mcm.spring
norm = mcolors.BoundaryNorm(np.arange(11), cmap.N)

ax = fig.add_subplot(1,1,1)
scat = ax.scatter(a,b,c=c, s=(d+10)*50, 
                  cmap=cmap,norm=norm)
fig.colorbar(scat, ax=ax, fraction=.45)

canvas.print_figure('../figures/cmapbubble.png', 
		facecolor='lightgray')
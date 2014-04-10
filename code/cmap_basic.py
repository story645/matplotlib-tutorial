"""
Example of matplotlib colormaps
http://matplotlib.org/1.3.1/api/artist_api.html?highlight=lines#module-matplotlib.lines
"""

import numpy as np

import matplotlib
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

data = np.random.randn(50,50)
print data
fig = figure.Figure(figsize=(12,6))

canvas = FigureCanvas(fig)

ax1 = fig.add_subplot(1,3,1)
#matplotlib can take any HTMLcolor

ax1.imshow(data, cmap='Blues')

ax2 = fig.add_subplot(1,3,2)
#matplotlib can take any HTMLcolor
ax2.imshow(data, cmap='Reds')

ax3 = fig.add_subplot(1,3,3)
#matplotlib can take any HTMLcolor
ax3.imshow(data, cmap='RdBu')

canvas.print_figure('../figures/pointcolor.png', 
		facecolor='lightgray')
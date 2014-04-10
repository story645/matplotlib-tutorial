"""
Example of creating a figure
"""
import numpy as np

from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

from mpl_toolkits.basemap import Basemap

data = np.random.random((180,360))

fig = figure.Figure()

canvas = FigureCanvas(fig)

ax = fig.add_subplot(1,1,1)
m = Basemap(projection='cyl', lat_0 = 50, lon_0 = -100,
                  ax=ax, resolution = 'l', area_thresh = 1000,
                  llcrnrlat=-90,urcrnrlat=90, llcrnrlon=-180,urcrnrlon=180)
				  
border_color = 'k'
m.drawcoastlines(color=border_color)
m.drawcountries(color=border_color)
m.drawmapboundary(color=border_color)
m.drawmapboundary(fill_color='white')
plt = m.imshow(data, interpolation='nearest')
fig.colorbar(plt, ax=ax, fraction=.15, 
			 orientation='horizontal')
                

canvas.print_figure('../figures/mapraster.png', 
		facecolor='lightgray')
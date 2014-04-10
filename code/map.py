"""
Example of creating a figure
"""
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

from mpl_toolkits.basemap import Basemap

fig = figure.Figure()

canvas = FigureCanvas(fig)

m = Basemap(projection='cyl', lat_0 = 50, lon_0 = -100,
                  ax=ax, resolution = 'l', area_thresh = 1000,
                  llcrnrlat=-90,urcrnrlat=90, llcrnrlon=-180,urcrnrlon=180)
				  
border_color = '0.8'
m.drawcoastlines(color=border_color)
m.drawcountries(color=border_color)
m.drawmapboundary(color=border_color)
                

canvas.print_figure('../figures/canvas.png', 
		facecolor='lightgray')
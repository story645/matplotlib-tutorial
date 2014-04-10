"""
Example of creating a figure
"""
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

fig = figure.Figure()

canvas = FigureCanvas(fig)

ax = fig.add_subplot(1,1,1)
m = Basemap(projection='cyl', lat_0 = 50, lon_0 = -100,
                  ax=ax, resolution = 'l', area_thresh = 1000,
                  llcrnrlat=-90,urcrnrlat=90, llcrnrlon=-180,urcrnrlon=180)
				  
border_color = '0.8'
m.drawcoastlines(color=border_color)
m.drawcountries(color=border_color)
m.drawmapboundary(color=border_color)

shp_info = m.readshapefile('st99_d00', 'states', drawbounds=True)
ax = fig.gca() # get current axes instance
non_states = ['District of Columbia','Puerto Rico']
statenames = [sp['NAME'] for sp in m.states_info if sp['NAME'] not in non_states]   
cls = ['r','g','b','y']
for nshape,seg in enumerate(m.states):
    poly = Polygon(seg, ec='k', fc=cls[nshape%4])
    ax.add_patch(poly)  

canvas.print_figure('../figures/mapshape.png', 
		facecolor='lightgray')
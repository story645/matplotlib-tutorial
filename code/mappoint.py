"""
Example of adding points to the plot

http://www.packtpub.com/article/plotting-geographical-data-using-basemap
"""
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

from mpl_toolkits.basemap import Basemap

# Cities names and coordinates
cities = ['London', 'New York', 'Madrid', 'Cairo', 'Moscow',
          'Delhi', 'Dakar']
lat = [51.507778, 40.716667, 40.4, 30.058, 55.751667,
       28.61, 14.692778]
lon = [-0.128056, -74, -3.683333, 31.229, 37.617778,
       77.23, -17.446667]

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

# map city coordinates to map coordinates
x, y = m(lon, lat)
m.scatter(x,y, s=100, c='red', zorder=100) 
for city, xc, yc in zip(cities, x, y):
	#draw the city name in a yellow (shaded) box
	ax.text(xc+5, yc, city,
		bbox=dict(facecolor='yellow', alpha=0.5))

canvas.print_figure('../figures/mappoint.png', 
		facecolor='lightgray')
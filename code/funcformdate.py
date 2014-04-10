"""
Set ticker properties
http://matplotlib.org/api/ticker_api.html
"""
import datetime

import numpy as np

import matplotlib
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

import matplotlib.ticker as mticker
import matplotlib.dates as mdates

fig = figure.Figure()
canvas = FigureCanvas(fig)

ax = fig.add_subplot(1,1,1)

ndays = 1000
index = [datetime.datetime.today() - datetime.timedelta(days=n) for n in range(ndays)][::-1]
values = np.random.randint(1,10, size=(ndays))

ax.plot(index, values, '-', linewidth=2, color='k')


days   = mdates.DayLocator()   # every year
months   = mdates.MonthLocator(interval=4)  # every month
xfmt = mdates.DateFormatter('%Y/%m/%d')
ax.xaxis.set_major_formatter(xfmt)
ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(days)

def funcf(val,pos):
	if val<5:
		return "under: %d"%val
	elif val>5:
		return "over: %d" %val
	else:
		return val
		

yfmt = mticker.FuncFormatter(funcf)
ax.yaxis.set_major_formatter(yfmt)

ax.grid(True)
#rotates and right aligns the date labels
fig.autofmt_xdate()
canvas.print_figure('../figures/textfuncdate.png', 
		facecolor='lightgray')
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 08 01:28:44 2014

@author: hannah
"""

import os 

import matplotlib
from matplotlib import figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib import pyplot as plt
from matplotlib import animation

import numpy as np

g = -9.8

matplotlib.rcParams['animation.convert_path'] = 'C:\Program Files\ImageMagick-6.8.6-Q16\convert.exe'
plt.xkcd()


S=500

ux = lambda t: np.exp(.01*t)*np.cos(t)
uy = lambda t: np.exp(.01*t)*np.sin(t)
t = np.arange(1,200,1)
x = [ux(ti) for ti in t]
y = [uy(ti) for ti in t]
xm = max(x)
ym = max(y)

fig = figure.Figure()
canvas = FigureCanvas(fig)
ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim((-xm,xm))    
ax.set_ylim((-ym,ym))
ax.grid(True)    
ax.axhline(0, color='k')
ax.axvline(0, color='k')

def animate(i):
    ax.plot(x[:i+1], y[:i+1], '--', color='orange', linewidth=3)  
    ax.plot(np.negative(x[:i+1]), np.negative(y[:i+1]), ':', color='darkblue', linewidth=3)
    ax.scatter(x[i],y[i], s=500, color='yellow', edgecolor='k', zorder=100)
    ax.scatter(-x[i], -y[i], s=500, color='blue', edgecolor='k', zorder=100)
    

anim = animation.FuncAnimation(fig, animate, frames=198, interval=20, blit=True)
anim.save('swirly.gif', writer='imagemagick')

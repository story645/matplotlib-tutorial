# -*- coding: utf-8 -*-
"""
Created on Tue Jul 01 01:22:23 2014

Modification of matplotlib colormap tutorial that shows the basemap colormaps
http://matplotlib.org/xkcd/examples/color/colormaps_reference.html

@author: hannah
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import cm
plt.xkcd()

maps=[m for m in cm.datad.keys() if not m.endswith("_r")]
maps.sort()

nrows = len(maps)
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

fig, axes = plt.subplots(nrows=nrows)
fig.suptitle("from mpl_toolkits.basemap import cm")

fig.subplots_adjust(top=0.90, bottom=0.01, left=0.2, right=0.99)


for ax, m in zip(axes, maps):
    ax.imshow(gradient, aspect='auto', cmap=cm.__dict__[m])
    pos = list(ax.get_position().bounds)
    x_text = pos[0] - 0.01
    y_text = pos[1] + pos[3]/2.
    fig.text(x_text, y_text, m, va='center', ha='right', fontsize=10)
    
for ax in axes:
    ax.set_axis_off()
    
plt.savefig('basemap_cms.png')

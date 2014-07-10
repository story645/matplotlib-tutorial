"""Simple gridspec example

http://matplotlib.org/users/gridspec.html
"""
import matplotlib.gridspec as gridspec

fig = plt.figure()
#create a grid of 2 rows, 3 columns for plots
gs = gridspec.GridSpec(2,3)
#put a plot in the first row, first column
ax1 = fig.add_subplot(gs[0,0])
#first row, second column
ax2 = fig.add_subplot(gs[0,1])
#first row, third column
ax3 = fig.add_subplot(gs[0,2])
#put a plot in the second row 
#have it span all three columns
ax4 = fig.add_subplot(gs[1,:])
fig.savefig("gridspec.png")

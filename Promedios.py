# lineplot.py                                                   
import numpy as np
import pylab as pl
# Make an array of x values
x = [7.0, 9.0, 8.5, 8.4]                                           
#Make an array of y values for each x value                                
y = [1, 2, 3, 4]
# use pylab to plot x and y                  
pl.plot(x, y, 'rp')
#Show the plot on the screen                             
pl.savefig('promedios.png')

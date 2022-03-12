import matplotlib.pyplot as plt
import numpy as np
import numba
import scipy
import math
from setting import max,min,accuracy,lim,lim2,function



x = np.linspace(min,max,accuracy)
y = np.linspace(min*1j,max*1j,accuracy)
X,Y = np.meshgrid(x,y)
Z = X+Y
# construct a complex plane
O = np.abs(function(Z))
    

# plot the output set 'O'
fig = plt.figure()
ax2 = plt.axes(projection ='3d')

ax2.plot_surface(Z.real,Z.imag,O)
fig.suptitle('Modular Surface', fontsize=16)
if(lim != None and lim2 != None):
    # set zlim in case of breakpoint.
    ax2.set_zlim(0,lim2)

plt.show()

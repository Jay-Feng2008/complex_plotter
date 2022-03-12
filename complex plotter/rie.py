from matplotlib import projections
import matplotlib.pyplot as plt
import numpy as np
import numba
import scipy
import math
from setting import min,max,accuracy,lim,lim2,function
# import all libraries that are possibly need

x = np.linspace(min,max,accuracy)
y = np.linspace(min*1j,max*1j,accuracy)
X,Y = np.meshgrid(x,y)
C = X+Y

F = function(C)

fig = plt.figure()
ax = fig.add_subplot(1,2,2,projection = '3d')
ax.plot_surface(C.real,C.imag,F.real)
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.plot_surface(C.real,C.imag,F.imag)

if (lim != None and lim2 != None):
    ax.set_zlim(lim,lim2)
    ax1.set_zlim(lim,lim2)
fig.suptitle('Riemann Surface', fontsize=16)

plt.show()



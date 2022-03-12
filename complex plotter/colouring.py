import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
from matplotlib.cm import ScalarMappable
from setting import max,min,accuracy,lim,lim2,function

def color(F):
    h = (np.pi - np.angle(F)) / (2.0 * np.pi)
    s = 1+0*F.real
    v = 1+0*F.real
    hsv = np.moveaxis((h, s, v), 0, -1)
    return matplotlib.colors.hsv_to_rgb(hsv)

fig, axes = plt.subplots(1, 1)
fig.suptitle('Domain Coloring', fontsize=16)
    
cbar = fig.colorbar(ScalarMappable(matplotlib.colors.Normalize(0, 2*np.pi), "hsv"),ax=axes)
cbar.set_ticks([0, np.pi, 2*np.pi])
cbar.set_ticklabels(["pi", "0 (2pi)", "pi"])

x = np.linspace(min,max,accuracy)
y = np.linspace(min*1j,max*1j,accuracy)
X,Y = np.meshgrid(x,y)
Z = X+Y

F = function(Z)
colors = color(F)
axes.imshow (colors,extent=(min,max,min,max))

plt.show()
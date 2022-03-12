import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
from matplotlib.cm import ScalarMappable
from setting import min,max,function

def f(z): 
    return function(z)

def grid(F):
    return (np.abs(np.sin(np.pi * np.real(f_val))) ** 0.1
            * np.abs(np.sin(np.pi * np.imag(f_val))) ** 0.1)

def line(F):
    h = 0*F.real
    s = 0*F.real
    v = grid(F)
    hsv = np.moveaxis((h,s,v), 0, -1)
    return matplotlib.colors.hsv_to_rgb(hsv)

fig, axes = plt.subplots(1, 1)
fig.suptitle('2D plot(2)',fontsize=16)

coords = np.linspace(min, max, 5000)
z_real, z_imag = np.meshgrid(coords, coords)
z = z_real + 1j * z_imag

f_val = f(z)

colors = line(f_val)
axes.imshow(colors,extent=(min,max,min,max))
    

plt.show()
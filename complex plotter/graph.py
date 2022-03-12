from setting import min,max,function,lim,lim2
import numpy as np
import matplotlib.pyplot as plt

spacing = (max-min)/10
accuracy = 500

a = []

for d in range(0,int(accuracy/10)):
    b = []
    for i in range(0,accuracy):
        b.append(min+i*((max-min)/accuracy)+(min+d*((abs(max)+abs(min))/(accuracy/10)))*1j)
    a.append(b)
b = []
for i in range(0,accuracy):
    b.append(min+i*((max-min)/accuracy)+max*1j)
a.append(b)

b = []
for i in range(0,len(a)):
    c = []
    for d in range(0,len(a[i])):
        c.append((a[i][d].imag)+(a[i][d].real)*1j)
    b.append(c)
c = []

fig = plt.figure()
for d in range (0,len(a)):
    a[d] = function(np.array(a[d]))
    plt.scatter(a[d].real,a[d].imag,c = 'blue',s = 0.5)

for d in range (0,len(b)):
    b[d] = function(np.array(b[d]))
    plt.scatter(b[d].real,b[d].imag,c = 'blue',s = 0.5)
fig.suptitle('2D plot', fontsize=16)

if (lim != None and lim2 != None):
    plt.xlim(left = lim,right = lim2)
    plt.ylim(bottom = lim,top = lim2)

    
plt.show()
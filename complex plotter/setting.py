import scipy
from numpy import sin,cos,exp,tan,sinh,cosh,tanh,log2,log10,sqrt,real,imag,arcsin,arccos,arctan,mod,pi,e
from numpy import log as ln
i = 1j
# libraries and crucial varibles

min = -5.0  # min real value that will be calculate
max = 5.0   # max real value that will be calculate
accuracy = 500  # default accuracy of 500 points, change in case of need(not recommend)
lim = -5  # lower limit of Z axie
lim2 = 5  # higer limit of Z axie
# if no limitations is need on Z axie, set lim,lim2 to 'None'

function = lambda z: z/(z**2-3) 
#function that will be plot, DO NOT change the parts before the ':'

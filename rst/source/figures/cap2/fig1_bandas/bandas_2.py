# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 14:06:09 2016

@author: pap
"""
from matplotlib import pyplot as plt
import matplotlib.collections as collections
import numpy as np

from mpl_toolkits.axes_grid1 import host_subplot

# eje x
ini = 0
fin = 16
l = np.linspace(ini, fin, num=1e5)
#figura
fig = plt.figure(edgecolor='w', facecolor='w', figsize=[20,5])

with plt.style.context('fivethirtyeight'):
    plt.plot(l, np.sin(l**2), lw=2, color='b')
#    plt.plot(x, np.sin(x) + 0.5 * x + np.random.randn(50))
#    plt.plot(x, np.sin(x) + 2 * x + np.random.randn(50))
# labels en x
xlab = (r'$10^{6}$', r'$10^{4}$', r'$10^{2}$', r'$10^{0}$', r'$10^{-2}$', r'$10^{-4}$',
        r'$10^{-6}$', r'$10^{-8}$', r'$10^{-10}$', r'$10^{-12}$', r'$10^{-14}$')
n = len(xlab)
med = float((fin-ini))/n
loclab = [med/2]
for i in range(1,n):
    loclab.append(med/2 + i*med)
plt.xticks(loclab, xlab)
ylim = [-1.25, 1.25]
plt.ylim(ylim)
plt.xlim([ini, fin])
plt.xlabel(r'Longitud de onda [m]', fontsize=20)
plt.yticks([0], ('0'))
plt.tick_params(labelsize=20)
plt.axes().set_axis_bgcolor('w')
plt.grid('off', axis='y')
plt.box('off'), 
#plt.title('Espectro electromagnético'.decode('utf-8'), fontsize=22)

ax = plt.twiny()
ax.set_xticks([2.6, 5.8, 7.6, 9., 10.5, 12.7, 14.8])
ax.set_xticklabels(['Radio', 'Microondas', 'Infrarrojo', 'Visible',
                    'Ultravioleta', 'Rayos X', r'Rayos $\gamma$'],
                    fontsize=18)

# marco ondas de radio
# ---- van desde 10^6 hasta el valor 10^0
# ---- es el punto medio entre xlab[2] y xlab[3]
radin = [0.]
radfin = [loclab[3]] # + (loclab[3] - loclab[2])/2
plt.axvspan(radin[0], radfin[0], ylim[0], ylim[1], facecolor=[.9, .4, .2], alpha=0.5)
# marco ondas de microondas
# ---- van desde 10^0 hasta el valor 10^-2
# ---- es el punto medio entre xlab[2] y xlab[3]
radin.append(radfin[0])
radfin.append(loclab[4])
plt.axvspan(radin[1], radfin[1], ylim[0], ylim[1], facecolor=[.2, .6, .2], alpha=0.5)
# marco ondas de infrarrojo
# ---- van desde 10^-1 hasta el valor 2.5*10^-6
# ---- es el punto medio entre xlab[2] y xlab[3]
radin.append(radfin[1])
radfin.append(loclab[6] - (1 - (1 - .78))*(loclab[6] - loclab[5])/2)
plt.axvspan(radin[2], radfin[2], ylim[0], ylim[1], facecolor=[.4, .6, .7], alpha=0.5)
# marco ondas de visible
# ---- van desde 4*10^-6 hasta el valor 7.8*10^-6
# ---- es el punto medio entre xlab[2] y xlab[3]
radin.append(radfin[2])
radfin.append(loclab[6] - (1 - (1 - .38))*(loclab[6] - loclab[5])/2 )
plt.axvspan(radin[3], radfin[3], ylim[0], ylim[1], facecolor=[.9, .9, .2], alpha=0.5)
# marco ondas de ultravioleta
# ---- van desde 2.5*10^-6 hasta el valor 7.80*10^-6
# ---- es el punto medio entre xlab[2] y xlab[3]
radin.append(radfin[3])
radfin.append((loclab[8] - loclab[7])/2 + loclab[7] )
plt.axvspan(radin[4], radfin[4], ylim[0], ylim[1], facecolor=[.5, .3, .67], alpha=0.5)
# marco ondas de rayos X
# ---- van desde 7.8*10^-6 hasta el valor *10^-12
# ---- es el punto medio entre xlab[2] y xlab[3]
radin.append(radfin[4])
radfin.append(loclab[9] )
plt.axvspan(radin[5], radfin[5], ylim[0], ylim[1], facecolor=[.3, .3, .8], alpha=0.5)
# marco ondas de rayos X
# ---- van desde 10^-12 hasta el valor *10^-14
# ---- es el punto medio entre xlab[2] y xlab[3]
radin.append(radfin[5])
radfin.append(fin)
plt.axvspan(radin[6], radfin[6], ylim[0], ylim[1], facecolor=[.3, .8, .2], alpha=0.5)
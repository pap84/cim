import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import numpy as np

ax = host_subplot(111, axes_class=AA.Axes)

# eje x
ini = 0
fin = 16
l = np.linspace(ini, fin, num=1e5)
#figura
#fig = plt.figure(edgecolor='w', facecolor='w', figsize=[20,5])

with plt.style.context('fivethirtyeight'):
    ax.plot(l, np.sin(l**2), lw=2, color='b')
    
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
plt.yticks([0], ('0'))
plt.tick_params(labelsize=20)
plt.axes().set_axis_bgcolor('w')
plt.grid('off', axis='y')
plt.box('off'), 
#plt.title('Espectro electromagnetico'.decode('utf-8'), fontsize=22)    

ax2 = ax.twin()  # ax2 is responsible for "top" axis and "right" axis
ax2.set_xticks([0., .5*np.pi, np.pi, 1.5*np.pi, 2*np.pi])
ax2.set_xticklabels(["texto", r"$\frac{1}{2}\pi$",
                     r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])

ax2.axis["right"].major_ticklabels.set_visible(False)


#plt.draw()
#plt.show()

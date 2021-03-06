from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from datos import data

d=data('mtcars')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d',  xlabel='Cylindres' , ylabel='Gears', zlabel='Frequency', title='Car Distribution by Gear and Cylindres') 
t1 = d.pivot_table( values = 'carb',index=['cyl'], columns = ['gear'], aggfunc = len)
x,y =t1.index, t1.columns 
xpos, ypos = np.meshgrid(x , y )
elements = len(x) * len(y)
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros(elements)
dx= np.ones_like(zpos)
dy=0.4 *np.ones_like(zpos)
dz=t1.values.flatten()
dz[np.isnan(dz)] = 0
c=['salmon','aqua','lightpink', 'salmon','aqua','lightpink','salmon','aqua','lightpink']
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=c, zsort='average')
plt.show()
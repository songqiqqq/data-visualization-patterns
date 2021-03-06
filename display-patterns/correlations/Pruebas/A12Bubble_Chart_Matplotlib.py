import numpy as np
import matplotlib.pyplot as plt
from datos import data

d=data('mtcars')
area = np.pi * (2 * d.cyl)**2  # 0 to 15 point radiuses
plt.scatter(d.wt, d.mpg, s=area, c='blue', alpha=0.5)
plt.title('Bubble Chart by Milles per Gallon and  Car Weight', family='serif', size=16)
plt.xlabel('Car Weight', family= 'serif')
plt.ylabel('Miles per Gallon', family='serif')
plt.show()
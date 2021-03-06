# PYTHON IMPLEMENTATION


## Data Set

For this example it was use Data Set called mtcars (Motor Trend Car Road Tests), which comes by default in R. This data was extracted from the 1974 Motor Trend US magazine, and comprises fuel consumption and 10 aspects of automobile design and performance for 32 automobiles (1973–74 models). 

To use this data set in Python, was used a Python module called rpy2. First create a file named as datos.py and write the next code.


~~~~{.python}
from rpy2.robjects import r
from rpy2.robjects import pandas2ri

def data(name):
        return pandas2ri.ri2py(r[name])
~~~~~~~~~~~~~



Then it is necessary import the datos.py file into the proyect, which you are working.


~~~~{.python}
from datos import data
d=data('mtcars')
~~~~~~~~~~~~~




## Dependences

* **rpy2:** Python interface to the R language (Gautier, 2016)[^1]. The rpy2 package is used to access all R datasets from Python.
* **Matplotlib:** is a python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. matplotlib can be used in python scripts, the python and ipython shell, web application servers, and six graphical user interface toolkits (Hunter, 2016)[^2].
* **Seaborn:** is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics (Waskom,2013)[^3].
* **Pyqtgraph**  is a pure-python graphics and GUI library built on PyQt4 / PySide and numpy. It is intended for use in mathematics / scientific / engineering applications (Campagnola, 2014)[^4].


## Code Example

### Matplotlib


The scatter function is used to make a Bubble Chart in Matplotlib, where x and y are sequence like objects of the same lengths and the size object is modified with *s* argument. The documentation for this function is available in [Scatter plot](http://matplotlib.org/api/pyplot_api.html?highlight=scatter#matplotlib.pyplot.scatter)



~~~~{.python}
import numpy as np
import matplotlib.pyplot as plt
from datos import data

d=data('mtcars')
area = np.pi * (2 * d.cyl)**2  # 0 to 15 point radiuses
plt.scatter(d.wt, d.mpg, s=area, c='blue', alpha=0.5)
plt.title('Bubble Chart by Milles per Gallon and  Car Weight',
family='serif', size=16)
plt.xlabel('Car Weight', family= 'serif')
plt.ylabel('Miles per Gallon', family='serif')
plt.show()
~~~~~~~~~~~~~

![](figures/A12Bubble_ChartPy_figure3_1.png)


The complete online documentation is also available at [matplotlib](http://matplotlib.org/contents.html).


### Seaborn

The function used to make a Bubble Chart in Seaborn is the same that Matplotlib (scatter). 


~~~~{.python}
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datos import data

d=data('mtcars')
sns.set(style="white")
g = sns.FacetGrid(d)
area = np.pi * (2 * d.cyl)**2
g.map(plt.scatter, "wt", "mpg",s=area)
plt.title("Scatterplot by Milles per Gallon and  Car Weight",
family='serif', size=16)
g.set_axis_labels("Car Weight","Milles per Gallon")
plt.show()
~~~~~~~~~~~~~

![](figures/A12Bubble_ChartPy_figure4_1.png)


The online documentation is available in [Seaborn](https://stanford.edu/~mwaskom/software/seaborn/api.html).


### Pyqtgraph

The function used to make a Bubble Chart is plot. With the size argument is changed the object size, which in this example represent the Number of cylinders. The documentation for this function is available in [Plot](http://www.pyqtgraph.org/documentation/functions.html#pyqtgraph.plot)


~~~~{.python}
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from datos import data

d=data('mtcars')
win = pg.GraphicsWindow()
win.resize(800,500)
win.setWindowTitle('Bubble Chart')
plt= win.addPlot(title="Scatterplots by Milles per Gallon and  Car
Weigh")
plt.plot(d.wt,d.mpg, pen=None, symbol='o', symbolSize=d.cyl,
symbolPen=(255,255,255,200), symbolBrush=(0,0,255,150))
plt.setLabel('left', "Miles per Gallon", units='mpg')
plt.setLabel('bottom', "Car Weight", units='lbs')

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore,
'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
~~~~~~~~~~~~~

![](figures/A12Bubble_ChartPy_figure5_1.png)


The complete online documentation is also available at [Pyqtrgaph](http://www.pyqtgraph.org/documentation/).


## References

[^1]: Gautier, Laurent (2016). rpy2. Consultado el 01 de Febrero, 2016 en http://rpy2.bitbucket.org/
[^2]: Hunter, John (2016). matplotlib. Consultado el 03 de Febrero, 2016 en http://matplotlib.org/
[^3]: Waskom, Michael (2016). Seaborn. Consultado el 08 de Febrero, 2016 en https://stanford.edu/~mwaskom/software/seaborn/index.htmltest/
[^4]: Campagnola, Luke (2014). Pyqtgraph. Consultado el 10 de Febrero, 2016 http://www.pyqtgraph.org/

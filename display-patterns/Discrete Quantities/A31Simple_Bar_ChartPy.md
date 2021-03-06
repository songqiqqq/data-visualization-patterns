# PYTHON IMPLEMENTATION

## Data Set

For this example it was used Data Set called mtcars (Motor Trend Car Road Tests), which comes by default in R. This data was extracted from the 1974 Motor Trend US magazine, and comprises fuel consumption and 10 aspects of automobile design and performance for 32 automobiles (1973–74 models). 

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

* **rpy2** Python interface to the R language (Gautier, 2016)[^1]. The rpy2 package is used to access all R datasets from Python.
* **Matplotlib** is a python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. matplotlib can be used in python scripts, the python and ipython shell, web application servers, and six graphical user interface toolkits (Hunter, 2016)[^2].
* **Seaborn** is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics (Waskom,2013)[^3].
* **Pyqtgraph**  is a pure-python graphics and GUI library built on PyQt4 / PySide and numpy. It is intended for use in mathematics / scientific / engineering applications (Campagnola, 2014)[^4].


## Code Example


### Matplotlib


~~~~{.python}
import matplotlib.pyplot as plt
from datos import data
import pandas

d=data('mtcars')
ps = pandas.Series([i for i in d.gear])
counts = ps.value_counts()

plt.bar(counts.index,counts,0.35, color="blue")
plt.title('Simple Bar Chart: Car Distribution ', family='serif',
size=16)
plt.xlabel('Number of Gears', family= 'serif')
plt.ylabel('Frequency', family='serif')
plt.show()
~~~~~~~~~~~~~

![](figures/A31Simple_Bar_ChartPy_figure3_1.png)


The complete online documentation is also available at [matplotlib](http://matplotlib.org/contents.html).


### Seaborn


~~~~{.python}
import seaborn as sns
import matplotlib.pyplot as plt
from datos import data
import pandas

d=data('mtcars')
ps = pandas.Series([i for i in d.gear])
counts = ps.value_counts()

sns.set(style="white", context="talk")

f, (ax1) = plt.subplots()
sns.barplot(counts.index, counts, palette="BuGn_d")
ax1.set_title("Simple Bar Chart: Car Distribution")
ax1.set_ylabel("Frequency")
ax1.set_xlabel("Number of Gears")
plt.show()
~~~~~~~~~~~~~

![](figures/A31Simple_Bar_ChartPy_figure4_1.png)


The online documentation is available in [Seaborn](https://stanford.edu/~mwaskom/software/seaborn/api.html).


### Pyqtgraph


~~~~{.python}
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from datos import data
import pandas

d=data('mtcars')
ps = pandas.Series([i for i in d.gear])
counts = ps.value_counts()

win = pg.plot(title='Simple Bar Chart')
bg1 = pg.BarGraphItem(x=counts.index, height=counts, width=0.6,
brush='b')
win.addItem(bg1)
win.setTitle('Simple Bar Chart: Car Distribution')
win.setLabel('left', "Frequency", )
win.setLabel('bottom', "Number of Gears")

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore,
'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
~~~~~~~~~~~~~

![](figures/A31Simple_Bar_ChartPy_figure5_1.png)


The complete online documentation is also available at [Pyqtrgaph](http://www.pyqtgraph.org/documentation/).


### References

[^1]: Gautier, Laurent (2016). rpy2. Consultado el 01 de Febrero, 2016 en http://rpy2.bitbucket.org/
[^2]: Hunter, John (2016). matplotlib. Consultado el 03 de Febrero, 2016 en http://matplotlib.org/
[^3]: Waskom, Michael (2016). Seaborn. Consultado el 08 de Febrero, 2016 en https://stanford.edu/~mwaskom/software/seaborn/index.htmltest/
[^4]: Campagnola, Luke (2014). Pyqtgraph. Consultado el 10 de Febrero, 2016 http://www.pyqtgraph.org/

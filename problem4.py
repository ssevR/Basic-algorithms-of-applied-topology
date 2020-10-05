#код взять https://github.com/AntonAyzenberg/Persistent-homology-Examples/blob/master/My_Persistence_test.ipynb
#!pip install --verbose git+https://github.com/mrzv/dionysus.git

import dionysus as d
import numpy as np


%matplotlib inline
import matplotlib.pyplot as plt
import networkx as nx
from IPython.display import clear_output
from mpl_toolkits.mplot3d import Axes3D


simplices = [([1], 0), ([2], 0), ([3], 0),
             ([1, 2], 2),
             ([4], 2.5),
             ([5], 3), ([2, 3], 3),
             ([3, 4], 3.7),
             ([1, 4], 4),
             ([1, 5], 4.3),
             ([4, 5], 5), ([1, 4, 5], 5),
             ([3, 5], 7.9), ([3, 4, 5], 7.9),
             ([6], 8),
             ([1, 6], 9),
             ([3, 6], 9),
             ([2, 6], 9.3), ([1, 2, 6], 9.3), ([2, 3, 6], 9.3),
             ([2, 5], 10.2), ([1, 2, 5], 10.2), ([2, 3, 5], 10.2),
             ([4, 6], 12), ([4, 6, 1], 12), ([4, 6, 3], 12)]

f = d.Filtration()
for vertices, time in simplices: f.append(d.Simplex(vertices, time))
f.sort()

m = d.homology_persistence(f)
dgms = d.init_diagrams(m, f)

d.plot.plot_diagram(dgms[0], show = False)
d.plot.plot_diagram(dgms[1], show = True)

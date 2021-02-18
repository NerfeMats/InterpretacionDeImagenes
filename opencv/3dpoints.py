# https://stackoverflow.com/questions/7275555/plotting-points-in-3d-from-text-file-using-matplotlib-or-octave
print('hola')

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed(101)
x,y,z = np.random.rand(3,20)

fig = plt.figure()
# version 1.0.x syntax:
#ax = fig.add_subplot(111, projection='3d')
# version 0.99.x syntax: (accepted by 1.0.x as well)
ax = Axes3D(fig)

ax.scatter(x,y,z)

fig.savefig('scatter3d.png')
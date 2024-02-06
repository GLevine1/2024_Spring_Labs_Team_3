import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
from numpy import pi
from mpl_toolkits import mplot3d 

#PRoblem 1 + 2
x = np.linspace(0, 2*pi, 100)
y = np.sin(x)
fig = plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, y, label='sine plot')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title("Plot of Sine over [0,2*pi]")
plt.show()

#problem 3
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm

plt.style.use('_mpl-gallery')

# Make data
X = np.arange(-10, 10, 0.25)
Y = np.arange(-10, 10, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
# Plot the surface
fig2 = fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues)

# ax.set(xticklabels=['x axis'],
#        yticklabels=['y axis'],
#        zticklabels=['z axis'])

plt.show()
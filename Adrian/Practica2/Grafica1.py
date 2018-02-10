from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

#Make data
X = np.arange(-5.12, 5.12, 0.005)
Y = np.arange(-5.12, 5.12, 0.005)

X, Y = np.meshgrid(X, Y)
Z = (X**2 + Y**2)

#Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap = cm.coolwarm, linewidth=0, antialiased=False)

#Add a color bar
fig.colorbar(surf)

plt.show()

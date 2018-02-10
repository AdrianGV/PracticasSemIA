from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

#Make data
X = np.arange(-2.048, 2.048, 0.005)
Y = np.arange(-2.048, 2.048, 0.005)

X, Y = np.meshgrid(X, Y)
Z = 100*(Y-X**2)**2+((X-1)**2)

#Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap = cm.coolwarm, linewidth=0, antialiased=False)

#Add a color bar
fig.colorbar(surf)

plt.show()

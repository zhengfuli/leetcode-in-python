from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

fig = plt.figure()
ax = Axes3D(fig)
x = np.arange(0, 4, 0.05)
y = 4 - x
X, Y = np.meshgrid(x, y)
Z = (4-X-Y)**2

x2 = np.arange(-4, 0, 0.05)
y2 = -4 - x2
X2, Y2 = np.meshgrid(x2, y2)
Z2 = (4+X2+Y2)**2

verts = [(0, -2, 0), (-2, 0, 0), (0, 2, 0), (2, 0, 0), (0, -2, 4), (-2, 0, 4), (0, 2, 4), (2, 0, 4)]
faces = [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], [1, 2, 6, 5], [2, 3, 7, 6], [0, 3, 7, 4]]
poly3d = [[verts[vert_id] for vert_id in face] for face in faces]
x1, y1, z1 = zip(*verts)
ax.scatter(x1, y1, z1)
ax.add_collection3d(Poly3DCollection(poly3d, facecolors='w', linewidths=2, alpha=0.1))
ax.add_collection3d(Line3DCollection(poly3d, colors='k', linewidths=0.8))

ax.plot([-4,4],[0,0],[0,0],label='beta1')
ax.plot([0,0],[-4,4],[0,0],label='beta2')
ax.plot([0,0],[0,0],[-2,18],label='RSS')


ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
ax.plot_surface(X2, Y2, Z2, rstride=1, cstride=1, cmap='rainbow')

ax.grid(True)

plt.xlabel('beta1')
plt.ylabel('beta2')
ax.set_zlabel('RSS')

plt.xlim((-4, 4))
plt.ylim((-4, 4))
plt.show()
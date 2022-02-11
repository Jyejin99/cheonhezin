# 3차원 그래프
'''
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

n = 100
xmin, xmax, ymin, ymax, zmin, zmax = 0, 20, 0, 20, 0, 50
cmin, cmax = 0, 2


xs = np.array([(xmax - xmin)*np.random.random_sample()+xmin for i in range(n)])
ys = np.array([(ymax - ymin)*np.random.random_sample()+ymin for i in range(n)])
zs = np.array([(zmax - zmin)*np.random.random_sample()+zmin for i in range(n)])
color = np.array([(cmax - cmin)*np.random.random_sample()+cmin for i in range(n)])

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs, ys, zs, c=color, marker='s', s=20, cmap='Oranges')

plt.show()
'''
# ----------------------
'''
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-10, 10, 11)
X = np.tile(x, (11, 1))
Y = np.transpose(X)
Z = 2 * np.random.rand(11, 11) - 1

surf = ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_zlim(-5, 5)
ax.set_xticks([-10, -5, 0, 5, 10])
ax.set_yticks([-10, -5, 0, 5, 10])
ax.set_zticks([-5, 0, 5])

fig.colorbar(surf, shrink=0.6, aspect=8)
surf.set_clim(-1.0, 1.0)
plt.tight_layout()
plt.show()
'''
# ---------------------
# 2차원 실시간 그래프
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random
import time

fig = plt.figure()     #figure(도표) 생성

ax = plt.subplot(211, xlim=(0, 50), ylim=(0, 1024))

max_points = 50

line, = ax.plot(np.arange(max_points), 
                np.ones(max_points, dtype=np.float)*np.nan, lw=1, c='blue',ms=1)

def init():
    return line

def animate(i):
    y = random.randint(0,1024)
    old_y = line.get_ydata()
    new_y = np.r_[old_y[1:], y]
    line.set_ydata(new_y)
    print(new_y)
    return line


anim = animation.FuncAnimation(fig, animate, init_func= init, frames=200, interval=50, blit=False)
plt.show()

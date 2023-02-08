from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import time
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

numbers = [0, 1, 0, 1, 3, 4, 6, 7, 8, 9, 10, 9, 7,6, 5, 6, 4, 6, 7, 9, 10, 12, 14, 17, 19, 19, 18, 15, 13, 14, 17, 19, 15, 13, 11, 10, 9, 7, 4, 3, 2, 5, 7, 8, 10, 11, 12, 14, 16, 19, 15, 12, 10, 11, 8, 6, 5, 3, 2, 1, 0, 0, 0]

xx, yy = np.meshgrid(np.linspace(0,1,640), np.linspace(0,1,480))

X = xx
Y = yy
Z = 10*np.ones(X.shape)

fig = plt.figure()

for _ in numbers:
    ax2 = fig.add_subplot(projection='3d')
    ax2.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=plt.imread('cd_13 {}.png'.format(_)), shade = False)    

    plt.axis('off')
    plt.show()
    plt.savefig('cd_3D {}'.format(_))

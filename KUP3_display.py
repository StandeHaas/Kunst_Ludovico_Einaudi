from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import time
import numpy as np 

fig = plt.figure()
ax = fig.add_subplot()

plt.ion()

def lst(max, i):
    lst = []
    n = 0
    for _ in range(i):
        lst.append(n)
        if n == 0:
            n += 1
        elif n >= max:
            n -= 1
        else:   
            n += np.random.choice([2,2,2,1,1,1,1,1,1,1,-1,-1,-1,-1,-1])
    return lst
numbers = [0, 1, 0, 1, 3, 4, 6, 7, 8, 9, 10, 9, 7,6,5, 6, 4, 5, 6, 7, 9, 10, 11, 12, 14, 16, 15, 16, 17, 15, 14, 16, 18, 19, 19, 18, 15, 13, 14, 17, 19, 15, 13, 11, 10, 9, 7, 4, 3, 2, 5, 7, 8, 10, 11, 12, 14, 16, 19, 15, 12, 10, 11, 8, 6, 5, 3, 2, 1, 0, 0, 0]


for _ in numbers:
    image = mpimg.imread('cd_4 {}.png'.format(_))
    plt.imshow(image)

    plt.axis('off')
    plt.show()
    fig.canvas.flush_events()


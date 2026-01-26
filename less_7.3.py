import matplotlib.pyplot as plt
import numpy as np
y = np.arange( -2, 2, 0.01)
x = y**2
plt.axis('equal')
plt.plot(x,y)
plt.savefig('function_static2.png')
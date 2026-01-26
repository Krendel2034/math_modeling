import matplotlib.pyplot as plt
import numpy as np
x = np.arange( -2, 2, 0.01)
y = x**3
plt.axis('equal')
plt.plot(x,y)
plt.savefig('function_static.png')
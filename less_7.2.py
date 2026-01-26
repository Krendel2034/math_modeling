import matplotlib.pyplot as plt
import numpy as np
x = np.arange( -2, 2, 0.01)
y = np.sin(x)
plt.axis('equal')
plt.plot(x,y)
plt.savefig('function_static1.png')
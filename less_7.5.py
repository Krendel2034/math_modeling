import matplotlib.pyplot as plt
import numpy as np
t = np.arange(-1,1, 0.1)
x = t 
y = t
plt.axis('equal')
plt.plot(x,y)
plt.savefig('function_static4.png')
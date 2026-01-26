import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0,  2*np.pi, 0.1)
x = np.sin(t) 
y = 2*np.cos(t)
plt.axis('equal')
plt.plot(x,y)
plt.savefig('function_static3.png')
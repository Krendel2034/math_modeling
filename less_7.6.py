import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
anim_obj, = plt.plot([], [])
def update(z_frame):
    A = z_frame
    x = np.arange(-4*np.pi, 4*np.pi, 0.01)
    y = A*np.sin(x)
    anim_obj.set_data(x, y)
    return anim_obj
A_ = np.arange(0.1 , 1.0, 0.05)
ani = FuncAnimation(fig, update, frames = A_)
ax.set_xlim(-4*np.pi, 4*np.pi)
ax.set_ylim(-4*np.pi, 4*np.pi)
ani.save('animation.gif')
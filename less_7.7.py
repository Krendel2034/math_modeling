import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
theta = np.linspace(0, 2*np.pi, 400) 
frame_centers_y = np.linspace(-1.0, 1.0, 3)  
A_array = [0.5, 1.0, 1.5] 
fig, ax = plt.subplots()
x_ellipse = np.cos(theta)  
y_ellipse = np.sin(theta)  
ellipse_line, = plt.plot([], [], lw=2)
def init():
    ax.set_xlim(-4*np.pi, 4*np.pi)
    ax.set_ylim(-4*np.pi, 4*np.pi)
    ellipse_line.set_data([], [])
    return ellipse_line,

def update(frame_idx):
    A = frame_idx 
    cy = 10.0 * np.sin(frame_idx)  
    cx = 10.0 * np.sin(frame_idx)  
    a = A
    b = 1.0 
    x = cx + a * np.cos(theta)
    y = cy + b * np.sin(theta)
    ellipse_line.set_data(x, y)
    return ellipse_line,
ani = FuncAnimation(fig, update, frames=A_array, init_func=init, blit=True)

ax.set_xlim(-4 * np.pi, 4 * np.pi) 
ax.set_ylim(-4 * np.pi, 4 * np.pi) 
ani.save('animation.gif')
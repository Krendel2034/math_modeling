import matplotlib.pyplot as plt
import numpy as np


def giperbola_plotter(a=1, b=1, c=0):

    x = np.arange(-10, 10, 0.01)
    y = 1/x

    plt.plot(x, y, label='my giperbola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title('giperbola plotter')
    plt.legend()

    plt.savefig('fig_5.png')


if __name__ == '__main__':
    giperbola_plotter()
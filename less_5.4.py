import matplotlib.pyplot as plt
import numpy as np


def circle_plotter(R=10):

    x = np.arange(-2*R, 2*R, 0.1)
    y = np.arange(-2*R, 2*R, 0.1)
    A = 5
    B = 3
    # Переход к неявнозаданным координатам
    X, Y = np.meshgrid(x, y)

    fxy = (X**2)/A + (Y**2)/B - 1

    # Команда рисования
    plt.contour(X, Y, fxy, levels=[0])
    # plt.axis('equal')

    plt.savefig('fig_6.png')


if __name__ == '__main__':
    circle_plotter()
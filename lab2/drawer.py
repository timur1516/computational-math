import numpy as np
from matplotlib import pyplot as plt

from lab2.util import _round


def draw_equation(x0, left, right, equation):
    side_step = abs(right - left) * 0.15
    l = left - side_step
    r = right + side_step

    plt.figure(figsize=(10, 6))

    x = np.linspace(l, r, 1000)
    y = equation.f(x)
    plt.plot(x, y, label=f'f(x)', color='blue')

    y0 = equation.f(x0)
    plt.scatter([x0], [y0], label=f'({_round(x0, 3)}; {_round(y0, 3)})', color='red', s=50)

    x_l = left
    y_l = equation.f(x_l)
    plt.vlines(x_l, 0, y_l, colors='black', linestyles='--')
    plt.scatter([x_l], [y_l], color='black', s=50)

    x_r = right
    y_r = equation.f(x_r)
    plt.vlines(x_r, 0, y_r, colors='black', linestyles='--')
    plt.scatter([x_r], [y_r], color='black', s=50)

    plt.axhline(0, color='black')

    plt.title(f'График функции f(x)={equation.text}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.xlim(l, r)
    plt.show()

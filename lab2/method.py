import numpy as np
from matplotlib import pyplot as plt

from lab2.result import Result
from lab2.util import _round


class Method:
    def __init__(self, equation, left, right, eps=1e-2, do_plot=False, do_log=False,
                 log_decimals=3):
        self.equation = equation
        self.left = left
        self.right = right
        self.eps = eps
        self.do_plot = do_plot
        self.do_log = do_log
        self.log_decimals = log_decimals
        self.iterations = 0
        self.log = []

    def solver(self):
        raise NotImplementedError()

    def log_header_creator(self):
        raise NotImplementedError()

    def _round(self, a):
        return _round(a, self.log_decimals)

    def draw(self, x0):
        side_step = abs(self.right - self.left) * 0.15
        l = self.left - side_step
        r = self.right + side_step

        plt.figure(figsize=(10, 6))

        x = np.linspace(l, r, 1000)
        y = self.equation.f(x)
        plt.plot(x, y, label=f'f(x)', color='blue')

        y0 = self.equation.f(x0)
        plt.scatter([x0], [y0], label=f'({self._round(x0)}; {self._round(y0)})', color='red', s=50)

        x_l = self.left
        y_l = self.equation.f(x_l)
        plt.vlines(x_l, 0, y_l, colors='black', linestyles='--')
        plt.scatter([x_l], [y_l], color='black', s=50)

        x_r = self.right
        y_r = self.equation.f(x_r)
        plt.vlines(x_r, 0, y_r, colors='black', linestyles='--')
        plt.scatter([x_r], [y_r], color='black', s=50)

        plt.axhline(0, color='black')

        plt.title(f'График функции f(x)={self.equation.text}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.xlim(l, r)
        # plt.savefig('plot.png')
        plt.show()

    def solve(self):
        if not self.equation.is_single_root_exist(self.left, self.right):
            raise Exception('На выбранном отрезке нет корней либо их больше одного')

        if self.do_log:
            self.log_header_creator()

        x = self.solver()

        if self.do_plot:
            self.draw(x)

        return Result(x, self.iterations, self.log if self.do_log else None)

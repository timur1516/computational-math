import numpy as np
from scipy.differentiate import derivative

from lab2.method import Method


class SimpleIterationsMethod(Method):
    def log_header_creator(self):
        self.log.append(['#', 'x_i', 'x_{i+1}', 'phi(x_{i+1})', 'f(x_{i+1})', 'delta'])

    def solver(self):
        f = self.equation.f
        f_ = self.equation.fst_derivative
        a = self.left
        b = self.right

        max_derivative = max(abs(f_(a)), abs(f_(b)))
        _lambda = 1 / max_derivative
        if f_(a) > 0: _lambda *= -1

        phi = lambda x: x + _lambda * f(x)

        phi_ = lambda x: derivative(phi, x).df
        q = np.max(abs(phi_(np.linspace(a, b, int(1 / self.eps)))))
        if q > 1:
            raise Exception(f'Метод не сходится так как значение q = {self._round(q)} >= 1')

        prev_x = a
        while True:
            self.iterations += 1
            x = phi(prev_x)
            delta = abs(x - prev_x)

            if self.do_log:
                self.log.append([
                    str(self.iterations),
                    str(self._round(prev_x)),
                    str(self._round(x)),
                    str(self._round(phi(x))),
                    str(self._round(f(x))),
                    str(self._round(delta))
                ])

            if delta <= self.eps:
                break

            prev_x = x

        return x

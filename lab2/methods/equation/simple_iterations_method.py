import numpy as np
from scipy.differentiate import derivative

from lab2.methods.equation.equation_method import EquationMethod


class SimpleIterationsMethod(EquationMethod):

    def solve(self):
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
            raise Exception(f'Метод не сходится так как значение q >= 1')

        prev_x = a
        while True:
            self.iterations += 1
            x = phi(prev_x)
            delta = abs(x - prev_x)

            self.log.append({
                'x_i': prev_x,
                'x_{i+1}': x,
                'phi(x_{i+1})': phi(x),
                'f(x_{i+1})': f(x),
                'delta': delta
            })

            if delta <= self.eps:
                break

            prev_x = x

        return x

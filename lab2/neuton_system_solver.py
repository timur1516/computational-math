import numpy as np

from lab2.equation import Equation
from lab2.system_of_equations import SystemOfEquations

a = SystemOfEquations([
    Equation(lambda x_: x_[0] ** 2 + x_[1] ** 2 - 4, 'ss'),
    Equation(lambda x_: -3 * x_[0] ** 2 + x_[1], 'fd')
])


def solver(x0, eps, system):
    x = x0

    while True:
        jcb = system.get_jacobi(x)
        b = system.get_value(x)
        dx = np.linalg.solve(np.array(jcb), -1 * np.array(b))
        nx = x + dx
        if np.max(np.abs(nx - x)) <= eps:
            break
        x = nx.tolist()

    return x


x = solver([1, 2], 1e-2, a)
print(x)

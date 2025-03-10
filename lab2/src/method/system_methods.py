import numpy as np

from lab2.src.result import Result


def newton_method(system, x0, eps):
    x = x0
    iterations = 0
    log = []
    while True:
        iterations += 1

        jcb = system.get_jacobi(x)
        b = system.get_value(x)
        dx = np.linalg.solve(np.array(jcb), -1 * np.array(b))
        nx = x + dx

        log.append({
            'x_i': x,
            'x_{i+1}': nx.tolist(),
            'dx': dx.tolist()
        })

        if np.max(np.abs(nx - x)) <= eps:
            break
        x = nx.tolist()

    return Result(x, iterations, log)

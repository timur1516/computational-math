import numpy as np

from lab2.src.methods.system.system_method import SystemMethod


class NewtonMethod(SystemMethod):

    def solve(self):
        x = self.point

        while True:
            self.iterations += 1

            jcb = self.system.get_jacobi(x)
            b = self.system.get_value(x)
            dx = np.linalg.solve(np.array(jcb), -1 * np.array(b))
            nx = x + dx

            self.log.append({
                'x_i': x,
                'x_{i+1}': nx.tolist(),
                'dx': dx.tolist()
            })

            if np.max(np.abs(nx - x)) <= self.eps:
                break
            x = nx.tolist()

        return x

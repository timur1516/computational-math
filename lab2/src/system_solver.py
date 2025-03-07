from lab2.src.methods.system.system_method_factory import SystemMethodFactory
from lab2.src.result import Result


class SystemSolver:
    def __init__(self, system, method_name, point, eps=1e-2):
        self.system = system
        self.point = point
        self.method = SystemMethodFactory.create(method_name, system, point, eps)

    def solve(self):
        x = self.method.solve()
        return Result(x, self.method.iterations, self.method.log)

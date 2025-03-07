from lab2.methods.equation.equation_method_factory import EquationMethodFactory
from lab2.result import Result


class EquationSolver:
    def __init__(self, equation, method_name, left, right, eps=1e-2):
        self.equation = equation
        self.left = left
        self.right = right
        self.method = EquationMethodFactory.create_method(method_name, equation, left, right, eps)

    def solve(self):
        if not self.equation.is_single_root_exist(self.left, self.right):
            raise Exception('На выбранном отрезке нет корней либо их больше одного')
        x = self.method.solve()
        return Result(x, self.method.iterations, self.method.log)

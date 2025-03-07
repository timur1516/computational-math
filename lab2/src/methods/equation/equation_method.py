from abc import abstractmethod


class EquationMethod:
    def __init__(self, equation, left, right, eps):
        self.equation = equation
        self.left = left
        self.right = right
        self.eps = eps
        self.log = []
        self.iterations = 0

    @abstractmethod
    def solve(self):
        pass

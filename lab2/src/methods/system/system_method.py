from abc import abstractmethod


class SystemMethod:
    def __init__(self, system, point, eps):
        self.system = system
        self.point = point
        self.eps = eps
        self.log = []
        self.iterations = 0

    @abstractmethod
    def solve(self):
        pass

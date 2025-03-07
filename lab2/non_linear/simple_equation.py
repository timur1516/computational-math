from scipy.differentiate import derivative


class SimpleEquation:
    def __init__(self, f, text):
        self.f = f
        self.text = text

    def __str__(self):
        return self.text

    def fst_derivative(self, x):
        return derivative(self.f, x).df

    def snd_derivative(self, x):
        return derivative(self.fst_derivative, x).df

    def is_single_root_exist(self, left, right):
        return self.f(left) * self.f(right) <= 0 <= self.fst_derivative(left) * self.fst_derivative(right)

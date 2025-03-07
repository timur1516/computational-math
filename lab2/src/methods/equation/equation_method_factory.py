from lab2.src.methods.equation.chord_method import ChordMethod
from lab2.src.methods.equation.secant_method import SecantMethod
from lab2.src.methods.equation.simple_iterations_method import SimpleIterationsMethod


class EquationMethodFactory:
    @staticmethod
    def create_method(method_name, equation, left, right, eps):
        if method_name == 'chord':
            return ChordMethod(equation, left, right, eps)
        if method_name == 'secant':
            return SecantMethod(equation, left, right, eps)
        if method_name == 'simple_iterations':
            return SimpleIterationsMethod(equation, left, right, eps)
        raise ValueError('Unknown method: %s' % method_name)

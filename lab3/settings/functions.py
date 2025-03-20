import math

from lab3.dto.function import Function

FUNCTIONS = [
    Function(lambda x: x ** 2, 'x^2'),
    Function(lambda x: math.sin(x), 'sin(x)'),
    Function(lambda x: x ** 3 - 3 * x ** 2 + 7 * x - 10, 'x^3 - 3x^2 + 7x - 10'),
    Function(lambda x: 5, '5')
]

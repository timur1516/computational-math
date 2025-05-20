from math import exp, sin, cos

from lab6.core.methods import euler_method, milne_method, improved_euler_method, second_order_runge_kutta_method, \
    fourth_order_runge_kutta_method, adams_method

ONE_STEP_METHODS = [
    euler_method,
    improved_euler_method,
    second_order_runge_kutta_method,
    fourth_order_runge_kutta_method
]

ONE_STEP_METHODS_NAMES = [
    'Метод Эйлера',
    'Модифицированный метод Эйлера',
    'Метод Рунге-Кутты 2-го порядка',
    'Метод Рунге-Кутты 4-го порядка',
]

RUNGE_P = [1, 2, 2, 4]

MULTY_STEP_METHODS = [
    adams_method,
    milne_method
]

MULTY_STEP_METHODS_NAMES = [
    'Метод Адамса',
    'Метод Милна'
]

EQUATIONS = [
    lambda x, y: y + (1 + x) * y ** 2,
    lambda x, y: x + y,
    lambda x, y: cos(x) - y
]

EQUATIONS_NAMES = [
    'y + (1 + x) * y^2',
    'x + y',
    'cos(x) - y'
]

EQUATIONS_SOLUTIONS = [
    lambda x, x0, y0: -exp(x) / (x * exp(x) - (x0 * exp(x0) * y0 + exp(x0)) / y0),
    lambda x, x0, y0: exp(x - x0) * (y0 + x0 + 1) - x - 1,
    lambda x, x0, y0: (y0 - sin(x0)) * exp(-(x - x0)) + sin(x)
]

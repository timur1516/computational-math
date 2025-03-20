import math

from lab3.dto.function import Function
from lab3.dto.result import Result
from lab3.settings.congif import INIT_N, MAX_ITERATIONS


def calculate_integral(function: Function, a: float, b: float, eps: float, method, runge_k: int) -> Result:
    n = INIT_N

    result = method(function, a, b, eps, n)
    iterations = 0
    delta = math.inf

    while delta > eps:
        if iterations >= MAX_ITERATIONS:
            raise Exception(f'Произведено {MAX_ITERATIONS} итераций, но ответ не найден')

        iterations += 1
        n *= 2

        new_result = method(function, a, b, eps, n)
        delta = abs(new_result - result) / (2 ** runge_k - 1)
        result = new_result

    return Result(result, n)

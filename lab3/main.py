from lab3.io.util import choose_options, read_float, print_result
from lab3.method.util import calculate_integral
from lab3.settings.constants import METHODS, METHODS_STRS, METHODS_RUNGE_K
from lab3.settings.functions import FUNCTIONS


def main():
    function_id = choose_options('Выберите функцию для интегрирования', FUNCTIONS) - 1
    function = FUNCTIONS[function_id]

    a = read_float('Введите нижний предел интегрирования')
    b = read_float('Введите верхний предел интегрирования')

    method_id = choose_options('Выберите метод для интегрирования', METHODS_STRS) - 1
    method = METHODS[method_id]
    runge_k = METHODS_RUNGE_K[method_id]

    eps = read_float('Введите точность')

    result = calculate_integral(function, a, b, eps, method, runge_k)

    print_result(result)


if __name__ == "__main__":
    main()

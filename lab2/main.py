from tabulate import tabulate

from lab2.chord_method import ChordMethod
from lab2.simple_equation import SimpleEquation
from lab2.secant_method import SecantMethod
from lab2.simple_iterations_method import SimpleIterationsMethod


def print_result(method):
    result = method.solve()
    print(f'Найденный корень: {result.x}')
    print(f'Потребовалось итераций: {result.iterations}')
    print('Лог решения:')
    print(tabulate(result.log[1:], result.log[:1][0], tablefmt='pretty'))


def main():
    equation = SimpleEquation(lambda x: x ** 3 - x + 4, 'x^3 - x + 4')
    chord_method = ChordMethod(equation, -2, -1, eps=1e-2, do_plot=True, do_log=True, log_decimals=5)
    secant_method = SecantMethod(equation, -2, -1, eps=1e-2, do_plot=True, do_log=True, log_decimals=5)
    simple_iterations_method = SimpleIterationsMethod(equation, -2, -1, eps=1e-2, do_plot=True, do_log=True,
                                                      log_decimals=5)
    print_result(chord_method)
    print_result(secant_method)
    print_result(simple_iterations_method)


if __name__ == '__main__':
    main()

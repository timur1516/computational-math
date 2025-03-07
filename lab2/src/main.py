import numpy as np

from lab2.src.drawer import draw_equation, draw_system
from lab2.src.equation_solver import EquationSolver
from lab2.src.io.reader import ConsoleReader, FileReader
from lab2.src.io.util import print_log, choose_options, read_filename, read_root_limits, read_eps, read_initial_point
from lab2.src.io.writer import ConsoleWriter, FileWriter
from lab2.src.non_linear.multi_equation import MultiEquation
from lab2.src.non_linear.simple_equation import SimpleEquation
from lab2.src.non_linear.system_of_equations import SystemOfEquations
from lab2.src.system_solver import SystemSolver

LOG_DECIMALS = 2
MODES = ['Нелинейное уравнение', 'Система нелинейных уравнений']
EQUATIONS = [
    SimpleEquation(lambda x: x ** 3 - x + 4, 'x^3 - x + 4'),
    SimpleEquation(lambda x: x ** 3 - x + 4, 'x^3 - x + 4')
]
SYSTEMS = [
    SystemOfEquations([
        MultiEquation(lambda x_: x_[0] ** 2 + x_[1] ** 2 - 4, 'x^2 + y^2 = 4'),
        MultiEquation(lambda x_: -3 * x_[0] ** 2 + x_[1], 'y = 3x^2')
    ]),
    SystemOfEquations([
        MultiEquation(lambda x_: x_[0] ** 2 + x_[1] ** 2 - 4, 'x^2 + y^2 = 4'),
        MultiEquation(lambda x_: x_[1] - np.sin(x_[0]), 'y = sin(x)')
    ])
]
EQ_METHODS_STRS = ['Метод хорд', 'Метод секущих', 'Метод простых итераций']
EQ_METHODS = ['chord', 'secant', 'simple_iterations']
SYS_METHODS_STRS = ['Метод Ньютона']
SYS_METHODS = ['newton']
IO_METHODS = ['Консоль', 'Файл']


def print_result(result, writer):
    writer.write(f'Найденный корень: {result.x}')
    writer.write(f'Потребовалось итераций: {result.iterations}')
    writer.write('Лог решения:')
    print_log(result.log, writer, LOG_DECIMALS)


def create_reader():
    intput_mode = choose_options('Выберите способ ввода границ интервала и точности', IO_METHODS)
    reader = ConsoleReader()
    if intput_mode == 2:
        filename = read_filename('r')
        reader = FileReader(filename)
    return reader


def create_writer():
    output_mode = choose_options('Выберите способ вывода ответа', IO_METHODS)
    writer = ConsoleWriter()
    if output_mode == 2:
        filename = read_filename('w')
        writer = FileWriter(filename)
    return writer


def main():
    mode = choose_options('Выберите что будете решать', MODES)

    if mode == 1:
        equation_id = choose_options('Выберите уравнение', EQUATIONS) - 1
        method_id = choose_options('Выберите метод', EQ_METHODS_STRS) - 1

        reader = create_reader()

        left, right = read_root_limits(reader)
        eps = read_eps(reader)
        equation_solver = EquationSolver(EQUATIONS[equation_id], EQ_METHODS[method_id], left, right, eps)
        result = equation_solver.solve()

        writer = create_writer()

        print_result(result, writer)
        draw_equation(result.x, left, right, equation_solver.equation)

    if mode == 2:
        system_id = choose_options('Выберите систему', SYSTEMS) - 1
        method_id = choose_options('Выберите метод', SYS_METHODS_STRS) - 1

        reader = create_reader()

        initial_point = read_initial_point(reader, SYSTEMS[system_id].n)
        eps = read_eps(reader)
        system_solver = SystemSolver(SYSTEMS[system_id], SYS_METHODS[method_id], initial_point, eps)
        result = system_solver.solve()

        writer = create_writer()

        print_result(result, writer)
        draw_system(result.x, initial_point, SYSTEMS[system_id])


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)

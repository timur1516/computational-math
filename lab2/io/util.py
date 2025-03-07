from tabulate import tabulate

from lab2.io.reader import FileReader


def print_log(log, writer, log_decimals):
    header = list(log[0].keys())
    data = [
        [f"{v:.{log_decimals}f}" if isinstance(v, (int, float)) else
         [f"{num:.{log_decimals}f}" for num in v] if isinstance(v, list) else str(v)
         for v in item.values()]
        for item in log
    ]
    writer.write(tabulate(data, header, tablefmt='pretty', showindex=True))


def choose_options(message, options):
    options_str = ''.join(f'{i + 1} -> {val}\n' for i, val in enumerate(options))
    print(f'{message}:\n{options_str}')
    result = None
    while result is None:
        try:
            result = int(input())
            if result not in range(1, len(options) + 1):
                print(f'Выберите один из вариантов:\n{options_str}')
                result = None
                continue
            break
        except:
            print('Значение должно быть числом. Попробуйте снова')
    return result


def read_root_limits(reader):
    left = None
    right = None
    while left is None or right is None:
        try:
            left, right = map(float, reader.read('Введите нижнюю и верхнюю границу диапазона корней: ').split())
        except:
            print('Значения должны быть числами!')
    return left, right


def read_eps(reader):
    eps = None
    while eps is None:
        try:
            eps = float(reader.read('Введите точность: '))
        except:
            print('Значение должно быть числом')
    return eps


def read_initial_point(reader, n):
    point = None
    while point is None:
        try:
            point = list(map(float, reader.read(f'Введите {n} координат начального приближения: ').split()))
            if len(point) != n:
                print(f'Введите {n} чисел!')
                point = None
        except:
            print('Значения должны быть числами!')
    return point


def read_filename():
    filename = None
    while filename is None:
        filename = input('Введите имя файла: ').strip()
        try:
            open(filename, 'r').close()
        except:
            filename = None
            print('Не удалось найти файл!')

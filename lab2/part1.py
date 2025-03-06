import numpy as np


def _r(n, precision):
    return "{:.{}f}".format(n, precision)


def f(x):
    return x ** 3 - 3.125 * (x ** 2) - 3.5 * x + 2.458


def f_(x):
    return 3 * (x ** 2) - 6.25 * x - 3.5


def f__(x):
    return 6 * x - 6.25


def fi(x):
    return x + (f(x)) / 7.75


def fi_1(x, y):
    return -np.cos(y - 2)


def fi_2(x, y):
    return np.sin(x + 0.5) - 1


def tab(l, r, step):
    for x in np.arange(l, r + step, step):
        print(f'{_r(x, 3)}\t{_r(f(x), 3)}')


def bin(a, b, EPS):
    cnt = 1
    while True:
        stop = False
        if abs(a - b) <= EPS:
            stop = True
        x = (a + b) / 2
        print(
            f'{cnt}\t{_r(a, 3)}\t{_r(b, 3)}\t{_r(x, 3)}\t{_r(f(a), 3)}\t{_r(f(b), 3)}\t{_r(f(x), 3)}\t{_r(abs(a - b), 3)}')
        if f(x) * f(a) <= 0:
            b = x
        else:
            a = x
        cnt += 1
        if stop:
            break


def _iter(x0, EPS):
    xk = x0
    cnt = 1
    while True:
        xkp = fi(xk)
        stop = False
        if abs(xk - xkp) <= EPS:
            stop = True
        print(f'{cnt}\t{_r(xk, 3)}\t{_r(xkp, 3)}\t{_r(f(xkp), 3)}\t{_r(abs(xk - xkp), 3)}')
        cnt += 1
        xk = xkp
        if stop:
            break


def neuton(x0, EPS):
    x_prev = x0
    cnt = 1
    while True:
        x_n = x_prev - f(x_prev) / f_(x_prev)
        print(
            f'{cnt}\t{_r(x_prev, 3)}\t{_r(f(x_prev), 3)}\t{_r(f_(x_prev), 3)}\t{_r(x_n, 3)}\t{_r(abs(x_prev - x_n), 3)}')
        if abs(x_n - x_prev) <= EPS:
            break
        x_prev = x_n
        cnt += 1


def iter_system(EPS):
    x = 0
    y = 0
    cnt = 1
    while True:
        x_n = fi_1(x, y)
        y_n = fi_2(x, y)
        print(
            f'{cnt}\t{_r(x, 3)}\t{_r(x_n, 3)}\t{_r(abs(x_n - x), 3)}\t{_r(y, 3)}\t{_r(y_n, 3)}\t{_r(abs(y_n - y), 3)}')
        if abs(x_n - x) <= EPS and abs(y_n - y) <= EPS:
            break
        x = x_n
        y = y_n
        cnt += 1


print('Табуляция')
tab(-5, 5, 0.5)
print('Половинное деление')
bin(-1.5, -1, 10 ** -2)
print('Значение первой производной в граничных точках')
print(_r(f_(0.5), 3))
print(_r(f_(1), 3))
print('Итерации')
_iter(1.0, 10 ** -2)
print('Условия для граничных точек')
print(_r(f(3.5) * f__(3.5), 3))
print(_r(f(4) * f__(4), 3))
print('Ньютон')
neuton(4, 10 ** -2)
print('Система')
iter_system(10 ** -2)

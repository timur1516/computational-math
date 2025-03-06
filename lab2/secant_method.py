from lab2.method import Method


class SecantMethod(Method):
    def log_header_creator(self):
        self.log.append(['#', 'x_{i-1}', 'x_i', 'x_{i+1}', 'f(x_{i+1})', 'delta'])

    def solver(self):
        f = self.equation.f
        f__ = self.equation.snd_derivative
        a = self.left
        b = self.right
        if f__(a) * f__(b) < 0:
            raise Exception(
                'Условия сходимости метода секущих не выполнены! Вторая производная не сохраняет знак на выбранном отрезке')
        x0 = a
        if f(a) * f__(a) > 0:
            x0 = a
        if f(b) * f__(b) > 0:
            x0 = b
        x1 = x0 + self.eps
        while True:
            self.iterations += 1

            x = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
            delta = abs(x - x1)

            if self.do_log:
                self.log.append([
                    str(self.iterations),
                    str(self._round(x0)),
                    str(self._round(x1)),
                    str(self._round(x)),
                    str(self._round(f(x))),
                    str(self._round(delta))
                ])

            if delta < self.eps:
                break

            x0 = x1
            x1 = x

        return x

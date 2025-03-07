from lab2.src.methods.equation.equation_method import EquationMethod


class SecantMethod(EquationMethod):

    def solve(self):
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

            self.log.append({
                'x_{i-1}': x0,
                'x_i': x1,
                'x_{i+1}': x,
                'f(x_{i+1})': f(x),
                'delta': delta
            })

            if delta < self.eps:
                break

            x0 = x1
            x1 = x

        return x

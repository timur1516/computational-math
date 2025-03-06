from lab2.method import Method


class ChordMethod(Method):

    def log_header_creator(self):
        self.log.append(['#', 'a', 'b', 'x', 'f(a)', 'f(b)', 'f(x)', 'delta'])

    def solver(self):
        f = self.equation.f
        a = self.left
        b = self.right
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        while True:
            self.iterations += 1
            if f(a) * f(x) <= 0:
                b = x
            else:
                a = x

            next_x = (a * f(b) - b * f(a)) / (f(b) - f(a))
            delta = abs(next_x - x)

            if self.do_log:
                self.log.append([
                    str(self.iterations),
                    str(self._round(a)),
                    str(self._round(b)),
                    str(self._round(x)),
                    str(self._round(f(a))),
                    str(self._round(f(b))),
                    str(self._round(f(x))),
                    str(self._round(delta))])

            if delta < self.eps:
                break

            x = next_x

        return x

from lab2.src.methods.equation.equation_method import EquationMethod


class ChordMethod(EquationMethod):

    def solve(self):
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

            self.log.append({
                'a': a,
                'b': b,
                'x': x,
                'f(a)': f(a),
                'f(b)': f(b),
                'f(x)': f(x),
                'delta': delta})

            if delta < self.eps:
                break

            x = next_x

        return x

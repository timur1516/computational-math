from lab3.settings.config import CONVERGENCE_EPS, BREAKING_POINTS_ACCURACY


class Function:
    def __init__(self, f, text):
        self.f = f
        self.text = text

    def compute(self, x):
        return self.f(x)

    def compute_or_none(self, x):
        try:
            val = self.compute(x)
            if abs(val) >= 1 / CONVERGENCE_EPS - 1 / BREAKING_POINTS_ACCURACY:
                return None
            return val
        except Exception:
            return None

    def __str__(self):
        return self.text
